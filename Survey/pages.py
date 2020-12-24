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
class survey_20(Page):
    form_model='player'
    form_fields=[
        'seoul_council_trust_metric',
        'seoul_council_policy_support_metric',
    ]
class survey_21(Page):
    form_model='player'
    form_fields=[
        'emergency_cash_injection_evaluation',
        'did_you_receive_emergency_cash_injection',
    ]
class survey_22(Page):
    form_model='player'
    form_fields=[
        'was_emergency_cash_injection_helpful',
    ]
    def is_displayed(self):
        return self.player.did_you_receive_emergency_cash_injection

class survey_23(Page):
    form_model='player'
    form_fields=[
        'after_nine_transportation_control_eval',
        'after_nine_transportation_control_experience_yesno',
    ]
class survey_24(Page):
    form_model='player'
    form_fields=[
        'after_nine_transportation_control_helpful_metric',
    ]
    def is_displayed(self):
        return self.player.after_nine_transportation_control_experience_yesno

class survey_25(Page):
    form_model='player'
    form_fields=[
        'crisis_emergency_support_eval',
        'did_you_receive_crisis_emergency_support',
    ]
class survey_26(Page):
    form_model='player'
    form_fields=[
        'was_crisis_emergency_support_helpful',
    ]
    def is_displayed(self):
        return self.player.did_you_receive_crisis_emergency_support
class survey_27(Page):
    form_model='player'
    form_fields=[
        'seoul_student_food_stamp_eval',
        'did_you_receive_food_stamp',

    ]
class survey_28(Page):
    form_model='player'
    form_fields=[
        'was_food_stamp_helpful',
    ]
    def is_displayed(self):
        return self.player.did_you_receive_food_stamp

class survey_29(Page):
    form_model='player'
    form_fields=[
        'free_online_learning_eval',
        'did_you_use_free_online_learning',
    ]
class survey_30(Page):
    form_model='player'
    form_fields=[
        'was_free_online_learning_helpful',
    ]
    def is_displayed(self):
        return self.player.did_you_use_free_online_learning

class survey_31(Page):
    form_model='player'
    form_fields=[
        'emergency_day_care_eval',
        'did_you_use_emergency_day_care',
    ]
class survey_32(Page):
    form_model='player'
    form_fields=[
        'was_emergency_day_care_helpful',
    ]
    def is_displayed(self):
        return self.player.did_you_use_emergency_day_care
class survey_33(Page):
    form_model='player'
    form_fields=[
        'weak_people_emergency_care_eval',
        'did_you_use_weak_people_emergency_care',
    ]
class survey_34(Page):
    form_model='player'
    form_fields=[
        'was_weak_people_emergency_care_helpful',
    ]
    def is_displayed(self):
        return self.player.did_you_use_weak_people_emergency_care

class survey_35(Page):
    form_model='player'
    form_fields=[
        'day_care_emergency_rearing_service_eval',
        'did_you_use_day_care_emergency_rearding_service',
    ]
class survey_36(Page):
    form_model='player'
    form_fields=[
        'was_day_care_emergency_rearing_service_helpful',
    ]
    def is_displayed(self):
        return self.player.did_you_use_day_care_emergency_rearding_service

class survey_37(Page):
    form_model='player'
    form_fields=[
        'zero_pay_linked_seoul_regional_currency_support_eval',
        'did_you_use_zero_pay_linked_seoul_regional_currency',
    ]
class survey_38(Page):
    form_model='player'
    form_fields=[
        'was_zero_pay_linked_seoul_regional_currency_helpful',
    ]
    def is_displayed(self):
        return self.player.did_you_use_zero_pay_linked_seoul_regional_currency


class survey_39(Page):
    form_model = 'player'
    form_fields = [
        'special_worker_free_lancer_support_eval',
        'did_you_receive_special_worker_free_lancer_support',
    ]


class survey_40(Page):
    form_model = 'player'
    form_fields = [
        'was_special_worker_free_lancer_support_helpful',
    ]
    def is_displayed(self):
        return self.player.did_you_receive_special_worker_free_lancer_support
class survey_41(Page):
    form_model='player'
    form_fields=[
        'psychological_counseling_eval',
        'did_you_use_psychological_counseling',
    ]
class survey_42(Page):
    form_model='player'
    form_fields=[
        'was_psychological_counseling_helpful',
    ]
    def is_displayed(self):
        return self.player.did_you_use_psychological_counseling
class survey_43(Page):
    form_model='player'
    form_fields=[
        'H1N1_countermeasure_overall_eval',
    ]

class survey_44(Page):
    form_model='player'
    form_fields=[
        'H1N1_countermeasure_bad_reason',
    ]
    def is_displayed(self):
        return self.player.H1N1_countermeasure_overall_eval==1
class survey_45(Page):
    form_model='player'
    form_fields=[
        'H1N1_countermeasure_good_reason',
    ]
    def is_displayed(self):
        return self.player.H1N1_countermeasure_overall_eval==5

class survey_46(Page):
    form_model='player'
    form_fields=[
        'pandemic_countermeasure_govt_role_how_important',
    ]
class survey_47(Page):
    form_model='player'
    form_fields=[
        'pandemic_countermeasure_govt_role_not_important_why',
    ]
    def is_displayed(self):
        return self.player.pandemic_countermeasure_govt_role_how_important==1

class survey_48(Page):
    form_model='player'
    form_fields=[
        'pandemic_countermeasure_govt_role_important_why',
    ]
    def is_displayed(self):
        return self.player.pandemic_countermeasure_govt_role_how_important==5
class survey_49(Page):
    form_model='player'
    form_fields=[
        'emergency_cash_injection_policy_eval',
        'did_you_receive_emergency_cash_injection_policy',
    ]
class survey_50(Page):
    form_model='player'
    form_fields=[
        'was_emergency_cash_injection_policy_helpful',
    ]
    def is_displayed(self):
        return self.player.did_you_receive_emergency_cash_injection_policy
class survey_51(Page):
    form_model='player'
    form_fields=[
        'post_covid_seoul_council_policy_1',
        'post_covid_seoul_council_policy_2',
        'post_covid_seoul_council_policy_3',
        'post_covid_seoul_council_policy_1_why',
        'post_covid_seoul_council_policy_2_why',
        'post_covid_seoul_council_policy_3_why',
    ]
class survey_52(Page):
    form_model='player'
    form_fields=[
        'when_did_you_move_to_the_district_year',
        'when_did_you_move_to_the_district_month',
        'where_did_you_reside_2016',
        'where_did_you_reside_2017',
        'where_did_you_reside_2018',
        'where_did_you_reside_2019',
        'where_did_you_reside_2020',
        'household_income',
        'high_class_standard',
        'middle_class_standard',
        'occupation',
        'special_worker_or_freelancer',
        'final_schooling',
        'health_state',
        'voted',
        'political_inclination',
    ]
class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [survey_1,survey_2,survey_3,survey_4,survey_5,survey_6,survey_7,survey_8,survey_9,survey_10,survey_11,
                 survey_12,survey_13,survey_14,survey_15,survey_16,survey_17,survey_18,survey_19,survey_20,survey_21,survey_22,
                 survey_23,survey_24,survey_25,survey_26,survey_27,survey_28,survey_29,survey_30,survey_31,survey_32, survey_33,survey_34,survey_35,survey_36,
                 survey_37,survey_38, survey_39,survey_40,survey_41,survey_42, survey_43, survey_44, survey_45, survey_46, survey_47, survey_48, survey_49, survey_50,survey_51,survey_52]
