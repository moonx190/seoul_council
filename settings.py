from os import environ


SESSION_CONFIGS = [
    {
        "name": "online_survey_t",
        "display_name": "test",
        "num_demo_participants": 1,
        "app_sequence": [
            "Intro",
            "Survey",
            "treatment",
            "iat",
            "survey_after_treatment",
            "Ending",
        ]
    },
    # {
    #     "name": "online_survey_q",
    #     "display_name": "서울시의회 온라인 설문조사 퀴즈처치",
    #     "num_demo_participants": 1,
    #     "app_sequence": [
    #         "Intro",
    #         "Survey",
    #         "quiz",
    #         "iat",
    #         "survey_after_treatment",
    #         "Ending",
    #     ]
    # },
    # {
    #     "name": "online_survey_c",
    #     "display_name": "서울시의회 온라인 설문조사 기준",
    #     "num_demo_participants": 1,
    #     "app_sequence": [
    #         "Intro",
    #         "Survey",
    #         "control",
    #         "iat",
    #         "survey_after_treatment",
    #         "Ending",
    #     ]
    # },
    # {
    #     "name": "online_survey_c2",
    #     "display_name": "서울시의회 온라인 설문조사 기준(무처치)",
    #     "num_demo_participants": 1,
    #     "app_sequence": [
    #         "Intro",
    #         "Survey",
    #         "iat",
    #         "survey_after_treatment",
    #         "Ending",
    #     ]
    # },
    # {
    #     "name": "treatment_only",
    #     "display_name": "처치",
    #     "num_demo_participants":1,
    #     "app_sequence": [
    #         "treatment",
    #     ]
    # },
    # {
    #     "name": "control_only",
    #     "display_name": "통제",
    #     "num_demo_participants": 1,
    #     "app_sequence": [
    #         "control",
    #     ]
    # },
    # {
    #     "name": "quiz",
    #     "display_name": "퀴즈",
    #     "num_demo_participants": 1,
    #     "app_sequence": [
    #         "Intro",
    #         "quiz",
    #         "Ending",
    #     ]
    # },
    {
        "name": "iat",
        "display_name": "IAT",
        "num_demo_participants": 1,
        "app_sequence": [
            "Intro",
            "iat",
            "Ending",
        ]
    },
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

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5l6yux%nrr(!nsaf$+8_eoqboic16x#ef6k)m3fvu936soen7i'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
