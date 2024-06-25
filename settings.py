from os import environ


SESSION_CONFIGS = [
    dict(
        name='cat_mbti_test',
        display_name="Cat MBTI Test",
        num_demo_participants=1,
        app_sequence=['personal_project'],
    ),
    dict(
        name='pauls_ai_experiment',
        display_name="Coding HW AI Detector",
        num_demo_participants=1,
        app_sequence=['pauls_experiment'],
    ),
dict(
        name='ai_experiment',
        display_name="Coding HW ChatGPT Detector",
        num_demo_participants=1,
        app_sequence=['ai'],
    ),
    dict(
        name='cards_base',
        display_name="Cards (baseline)",
        cards_exchange_rate=100.0,
        cards_treatment='baseline',
        cards_report_1_payoff=2,
        cards_report_2_payoff=4,
        cards_report_3_payoff=6,
        cards_report_4_payoff=8,
        cards_report_5_payoff=10,
        cards_cutoff_percentage=20,
        cards_fixed_penalty=5,
        cards_choice_percentage=50,
        cards_random_penalty_a=3,
        cards_random_penalty_b=7,
        cards_pause_at_start=False,
        num_demo_participants=1,
        real_world_currency_per_point=0.01,
        app_sequence=['cards'],
        doc='cards_treatment can be one of: [baseline, fixed, random, maximum, minimum]',
    ),
    dict(
        name='cards_fixed',
        display_name="Cards (fixed)",
        cards_exchange_rate=100.0,
        cards_treatment='fixed',
        cards_report_1_payoff=2,
        cards_report_2_payoff=4,
        cards_report_3_payoff=6,
        cards_report_4_payoff=8,
        cards_report_5_payoff=10,
        cards_cutoff_percentage=20,
        cards_fixed_penalty=5,
        cards_choice_percentage=50,
        cards_random_penalty_a=3,
        cards_random_penalty_b=7,
        cards_pause_at_start=False,
        num_demo_participants=1,
        real_world_currency_per_point=0.01,
        app_sequence=['cards'],
        doc='cards_treatment can be one of: [baseline, fixed, random, maximum, minimum]',
    ),
    dict(
        name='cards_random',
        display_name="Cards (random)",
        cards_exchange_rate=100.0,
        cards_treatment='random',
        cards_report_1_payoff=2,
        cards_report_2_payoff=4,
        cards_report_3_payoff=6,
        cards_report_4_payoff=8,
        cards_report_5_payoff=10,
        cards_cutoff_percentage=20,
        cards_fixed_penalty=5,
        cards_choice_percentage=50,
        cards_random_penalty_a=3,
        cards_random_penalty_b=7,
        cards_pause_at_start=False,
        num_demo_participants=1,
        real_world_currency_per_point=0.01,
        app_sequence=['cards'],
        doc='cards_treatment can be one of: [baseline, fixed, random, maximum, minimum]',
    ),
    dict(
        name='cards_min',
        display_name="Cards (minimum)",
        cards_exchange_rate=100.0,
        cards_treatment='minimum',
        cards_report_1_payoff=2,
        cards_report_2_payoff=4,
        cards_report_3_payoff=6,
        cards_report_4_payoff=8,
        cards_report_5_payoff=10,
        cards_cutoff_percentage=20,
        cards_fixed_penalty=5,
        cards_choice_percentage=50,
        cards_random_penalty_a=3,
        cards_random_penalty_b=7,
        cards_pause_at_start=False,
        num_demo_participants=1,
        real_world_currency_per_point=0.01,
        app_sequence=['cards'],
        doc='cards_treatment can be one of: [baseline, fixed, random, maximum, minimum]',
    ),
    dict(
        name='cards_max',
        display_name="Cards (maximum)",
        cards_exchange_rate=100.0,
        cards_treatment='maximum',
        cards_report_1_payoff=2,
        cards_report_2_payoff=4,
        cards_report_3_payoff=6,
        cards_report_4_payoff=8,
        cards_report_5_payoff=10,
        cards_cutoff_percentage=20,
        cards_fixed_penalty=5,
        cards_choice_percentage=50,
        cards_random_penalty_a=3,
        cards_random_penalty_b=7,
        cards_pause_at_start=False,
        num_demo_participants=1,
        real_world_currency_per_point=0.01,
        app_sequence=['cards'],
        doc='cards_treatment can be one of: [baseline, fixed, random, maximum, minimum]',
    ),
    dict(
        name='cards_minbelief',
        display_name="Cards (minimum) plus belief",
        cards_exchange_rate=100.0,
        cards_treatment="minimum",
        cards_report_1_payoff=2,
        cards_report_2_payoff=4,
        cards_report_3_payoff=6,
        cards_report_4_payoff=8,
        cards_report_5_payoff=10,
        cards_cutoff_percentage=20,
        cards_fixed_penalty=5,
        cards_choice_percentage=50,
        cards_random_penalty_a=3,
        cards_random_penalty_b=7,
        cards_pause_at_start=False,

        cb_num_previous_students=90,
        cb_previous_school="UCSD",
        cb_guess_range=0.5,
        cb_correct_answer=5,
        cb_correct_pay=1,
        cb_exchange_rate=1.0,
        num_demo_participants=1,
        real_world_currency_per_point=0.01,
        app_sequence=['cards','cards_belief'],
        doc='cards_treatment can be one of: [baseline, fixed, random, maximum, minimum]',
    ),
    dict(
        name='cards_maxbelief',
        display_name="Cards (maximum) plus belief",
        cards_exchange_rate=100.0,
        cards_treatment="maximum",
        cards_report_1_payoff=2,
        cards_report_2_payoff=4,
        cards_report_3_payoff=6,
        cards_report_4_payoff=8,
        cards_report_5_payoff=10,
        cards_cutoff_percentage=20,
        cards_fixed_penalty=5,
        cards_choice_percentage=50,
        cards_random_penalty_a=3,
        cards_random_penalty_b=7,
        cards_pause_at_start=False,

        cb_num_previous_students=90,
        cb_previous_school="UCSD",
        cb_guess_range=0.5,
        cb_correct_answer=5,
        cb_correct_pay=1,
        cb_exchange_rate=1.0,
        num_demo_participants=1,
        real_world_currency_per_point=0.01,
        app_sequence=['cards','cards_belief'],
        doc='cards_treatment can be one of: [baseline, fixed, random, maximum, minimum]',
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '%ueo=aehsl61&y%7czbg_3s55k1*x_tt63sc3(0dwsuu#wve%a'

INSTALLED_APPS = ['otree']
