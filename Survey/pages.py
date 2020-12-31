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

class survey_7(Page):
    form_model='player'
    form_fields=[
        'COVID_infected_yesno',
        'COVID_infected_neighbors_yesno',
        'COVID_test_yesno',
    ]
class survey_8(Page):
    form_model='player'
    form_fields=[
        'COVID_test_reason',
    ]
    def is_displayed(self):
        return self.player.COVID_test_yesno==True
class survey_9(Page):
    form_model='player'
    form_fields=[
        'COVID_how_severe',
        'COVID_domestic_how_severe',
        'COVID_health_effect_how_severe',
        'COVID_financial_effect_how_severe',
        'COVID_social_effect_how_severe',
    ]
class survey_10(Page):
    form_model='player'
    form_fields=[
        'COVID_health_effect_experience',
        'COVID_jobloss_experience',
        'COVID_incomeloss_experience',
        'COVID_emotional_experience',
    ]
    def is_displayed(self):
        return self.player.COVID_infected_yesno

class survey_11(Page):
    form_model='player'
    form_fields=[
        'COVID_potential_infection_channel_1',
        'COVID_potential_infection_channel_2',
        'COVID_fear_which',
        'pe_1',
        'pe_2',
        'pe_3',
        'pe_4',
        'pe_5',
    ]
    def vars_for_template(self) -> dict:
        vars_to_return = {}
        vars_to_return['COVID_EFFECTIVENESS_METRIC']=[i[1] for i in Constants.COVID_EFFECTIVENESS_METRIC]
        return vars_to_return
class survey_12(Page):
    form_model='player'
    form_fields=[
        'COVID_info_routinely',
        'COVID_info_source',
        'COVID_info_type_1',
        'COVID_info_type_2',
        'COVID_info_enough',
    ]
class survey_13(Page):
    form_model='player'
    form_fields=[
        'COVID_termination_time',
        'COVID_termination_time_reason',
        'COVID_termination_time_reason_op',
        'do_you_trust_govt_prospection_for_end_of_COVID',
        'p1',
        'p2',
        'p3',
        'p4',
        'p5',
        'p6',
    ]

    def vars_for_template(self) -> dict:
        vars_to_return = {}
        vars_to_return['PROSPECT_METRIC'] = [i[1] for i in Constants.PROSPECT_METRIC]
        return vars_to_return

class survey_14(Page):
    form_model='player'
    form_fields=[
        't1',
        't2',
        't3',
        't4',
        't5',
        't6',
        't7',
    ]

    def vars_for_template(self) -> dict:
        vars_to_return = {}
        vars_to_return['TRUST_METRIC'] = [i[1] for i in Constants.TRUST_METRIC]
        return vars_to_return
class survey_15(Page):
    form_model='player'
    form_fields=[
        'COVID_countermeasure_overall_eval'
    ]
class survey_16(Page):
    form_model='player'
    form_fields=[
        'COVID_countermeasure_welldone_reason',
    ]
    def is_displayed(self):
        return self.player.COVID_countermeasure_overall_eval==1 or self.player.COVID_countermeasure_overall_eval==2
class survey_17(Page):
    form_model='player'
    form_fields=[
        'COVID_countermeasure_wrongdoing_reason',
    ]
    def is_displayed(self):
        return self.player.COVID_countermeasure_overall_eval==3 or self.player.COVID_countermeasure_overall_eval==4
class survey_18(Page):
    form_model='player'
    form_fields=[
        'COVID_policy_info_source',
    ]
class survey_19(Page):
    form_model = 'player'
    form_fields=[
        'COVID_countermeasure_social_distancing_evaluation',
        'social_distancing_overreaction',
        'social_distancing_overreaction_op',
        'social_distancing_underreaction',
        'social_distancing_underreaction_op',
    ]

page_sequence = [survey_1,survey_2,survey_3,survey_4,survey_5,survey_6,survey_7,survey_8,survey_9,survey_10,survey_11,
                 survey_12,survey_13,survey_14,survey_15,survey_16,survey_17,survey_18,survey_19,]
