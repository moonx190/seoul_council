from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class survey_1(Page):
    form_model = 'player'
    form_fields = [
        'gender',
        'birth_year',
        'district',
    ]
class survey_2(Page):
    form_model='player'
    form_fields=[
        'seoul_council_member_in_residential_district_knowledge',

    ]
class survey_3(Page):
    form_model='player'
    form_fields=[
        'seoul_council_member_in_residential_district_party_knowledge',
        'seoul_council_in_residential_district_policy_knowledge',

    ]
    def is_displayed(self):
        return self.player.seoul_council_member_in_residential_district_knowledge==True
class survey_4(Page):
    form_model='player'
    form_fields=[
        'seoul_council_in_residential_district_channel_1',
        'seoul_council_in_residential_district_channel_2',
        'seoul_council_in_residential_district_channel_3',
        'seoul_council_in_residential_district_channel_4',
        'seoul_council_in_residential_district_channel_5',
        'seoul_council_in_residential_district_channel_6',
        'seoul_council_in_residential_district_channel_7',
        'seoul_council_in_residential_district_channel_8',
        'seoul_council_in_residential_district_channel_9',
        'seoul_council_in_residential_district_channel_10',
        'seoul_council_in_residential_district_channel_11',
        'seoul_council_member_in_residential_district_opinion',
    ]
class survey_5(Page):
    form_model='player'
    form_fields=[
        'seoul_council_member_in_residential_district_positive',
    ]
    def is_displayed(self):
        return (self.player.seoul_council_member_in_residential_district_opinion==1 or self.player.seoul_council_member_in_residential_district_opinion==2) \
               and (self.player.seoul_council_member_in_residential_district_opinion !=5)


class survey_6(Page):
    form_model='player'
    form_fields=[
        'seoul_council_member_in_residential_district_negative',
    ]
    def is_displayed(self):
        return (self.player.seoul_council_member_in_residential_district_opinion == 3 or self.player.seoul_council_member_in_residential_district_opinion == 4)\
               and (self.player.seoul_council_member_in_residential_district_opinion != 5)
class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [survey_1,survey_2,survey_3,survey_4,survey_5,survey_6]
