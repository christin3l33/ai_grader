from otree.api import *
from openai import OpenAI
from thefuzz import fuzz
import time


doc = """
Students will get their Python codes graded
"""
author = 'leeevm@bc.edu'


class C(BaseConstants):
    NAME_IN_URL = 'ai_code_detector'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    QUESTION_1 = 'Write a Python program that checks if two strings are anagrams or not.'


class Subsession(BaseSubsession):
    q1_gpt_response = models.LongStringField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1_time_on_page = models.FloatField(blank=True)
    q1_user_response = models.LongStringField(label='Write a Python program that checks if two strings are anagrams or not.')
    q1_user_explanation = models.LongStringField(label='Please explain your code. ')
    q1_ratio_similarity = models.IntegerField()
    q1_token_sort_ratio_similarity = models.IntegerField()
    q1_token_set_ratio_similarity = models.IntegerField()
    q1_mean_similarity = models.FloatField()
    q1_correct = models.IntegerField()


def generate_ai_code(player: Player):
    subsession = player.subsession

    all_questions = [C.QUESTION_1]
    gpt_responses = []

    for question in all_questions:
        client = OpenAI(
            api_key='sk-proj-FvgOHsfo2yveBzxyZoMqT3BlbkFJaMl8nT9W3CWsWR8wn6CF'
        )

        prompt = "Please only write the code; no explanation necessary.\n\n" + question
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="gpt-3.5-turbo",
        )

        gpt_responses.append(chat_completion.choices[0].message.content)

    subsession.q1_gpt_response = gpt_responses[0]


def check_similarity(player: Player):
    subsession = player.subsession

    human_code = player.q1_user_response
    ai_code = subsession.q1_gpt_response

    player.q1_ratio_similarity = fuzz.ratio(human_code, ai_code)
    player.q1_token_sort_ratio_similarity = fuzz.token_sort_ratio(human_code, ai_code)
    player.q1_token_set_ratio_similarity = fuzz.token_set_ratio(human_code, ai_code)

    mean = (player.q1_ratio_similarity + player.q1_token_sort_ratio_similarity + player.q1_token_set_ratio_similarity) / 3

    mean_rounded = round(mean, 2)

    player.q1_mean_similarity = mean_rounded


def check_correct(player: Player):
    with open('user_q1.py', 'w') as file:
        file.write(player.q1_user_response)
    replacement_line = "def anagram(word1, word2):\n"

    f = open('user_q1.py')
    first_line, remainder = f.readline(), f.readlines()
    t = open('user_q1.py', 'w')
    t.write(replacement_line)
    t.writelines(remainder)
    t.close()

    with open('user_q1.py', 'r') as file:
        from user_q1 import anagram

        answer = anagram("fried", "fired")
        player.q1_correct = 0
        if answer == True:
            player.q1_correct += 1
        else:
            player.q1_correct += 0


class Q1(Page):
    form_model = 'player'
    form_fields = ['q1_user_response']
    timeout_seconds = 600

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        player.participant.vars['start_time'] = time.time()
        return True

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        generate_ai_code(player)
        check_similarity(player)
        check_correct(player)

        start_time = player.participant.vars.get('start_time', None)
        if start_time:
            time_difference = time.time() - start_time
            time_on_page_float = round(time_difference, 2)
            player.q1_time_on_page = time_on_page_float


class Q1Correct(Page):
    pass


class Q1Detection(Page):
    form_model = 'player'
    form_fields = ['q1_user_explanation']

    @staticmethod
    def is_displayed(player: Player):
        return player.q1_time_on_page < 120 or player.q1_mean_similarity > 80


class Result(Page):
    form_model = 'player'


page_sequence = [
    Q1, Q1Correct, Q1Detection, Result
    ]