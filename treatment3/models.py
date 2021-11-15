from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from Global_Constants import GlobalConstants

author = '조남운'

doc = """
2021 cov19 금연지원정책 프레임3
"""


class Constants(BaseConstants):
    name_in_url = 'treatment3'
    players_per_group = None
    num_rounds = 1

    WAITING_SECONDS = GlobalConstants.WAITING_SECONDS


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.IntegerField(initial=3)
