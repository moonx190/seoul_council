from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class survey_1(Page):
    form_model = 'player'
    form_fields = [
        'seoul_council_member_in_residential_district_knowledge',
        'seoul_council_member_in_residential_district_party_knowledge',
        'seoul_council_in_residential_district_policy_knowledge',
        'seoul_council_in_residential_district_channel',
    ]



class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [survey_1,]
