from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from Global_Constants import GlobalConstants


author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
코로나19등 신종감염병 대응을 위한 국가금연지원사업 전략 개발
"""


class Constants(BaseConstants):
    name_in_url = 'introduction'
    players_per_group = None
    num_rounds = 1

    EXCHANGE_RATE = GlobalConstants.EXCHANGE_RATE


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    panel_id = models.StringField()
