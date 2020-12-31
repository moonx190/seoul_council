from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class survey_20(Page):
    form_model = 'player'
    form_fields = [
        'seoul_council_trust_metric',
        'seoul_council_policy_support_metric',
    ]


class survey_21(Page):
    form_model = 'player'
    form_fields = [
        'emergency_cash_injection_evaluation',
        'did_you_receive_emergency_cash_injection',
    ]


class survey_22(Page):
    form_model = 'player'
    form_fields = [
        'was_emergency_cash_injection_helpful',
    ]

    def is_displayed(self):
        return self.player.did_you_receive_emergency_cash_injection


class survey_23(Page):
    form_model = 'player'
    form_fields = [
        'after_nine_transportation_control_eval',
        'after_nine_transportation_control_experience_yesno',
    ]


class survey_24(Page):
    form_model = 'player'
    form_fields = [
        'after_nine_transportation_control_helpful_metric',
    ]

    def is_displayed(self):
        return self.player.after_nine_transportation_control_experience_yesno


class survey_25(Page):
    form_model = 'player'
    form_fields = [
        'crisis_emergency_support_eval',
        'did_you_receive_crisis_emergency_support',
    ]


class survey_26(Page):
    form_model = 'player'
    form_fields = [
        'was_crisis_emergency_support_helpful',
    ]

    def is_displayed(self):
        return self.player.did_you_receive_crisis_emergency_support


class survey_27(Page):
    form_model = 'player'
    form_fields = [
        'seoul_student_food_stamp_eval',
        'did_you_receive_food_stamp',

    ]


class survey_28(Page):
    form_model = 'player'
    form_fields = [
        'was_food_stamp_helpful',
    ]

    def is_displayed(self):
        return self.player.did_you_receive_food_stamp


class survey_29(Page):
    form_model = 'player'
    form_fields = [
        'free_online_learning_eval',
        'did_you_use_free_online_learning',
    ]


class survey_30(Page):
    form_model = 'player'
    form_fields = [
        'was_free_online_learning_helpful',
    ]

    def is_displayed(self):
        return self.player.did_you_use_free_online_learning


class survey_31(Page):
    form_model = 'player'
    form_fields = [
        'emergency_day_care_eval',
        'did_you_use_emergency_day_care',
    ]


class survey_32(Page):
    form_model = 'player'
    form_fields = [
        'was_emergency_day_care_helpful',
    ]

    def is_displayed(self):
        return self.player.did_you_use_emergency_day_care


class survey_33(Page):
    form_model = 'player'
    form_fields = [
        'weak_people_emergency_care_eval',
        'did_you_use_weak_people_emergency_care',
    ]


class survey_34(Page):
    form_model = 'player'
    form_fields = [
        'was_weak_people_emergency_care_helpful',
    ]

    def is_displayed(self):
        return self.player.did_you_use_weak_people_emergency_care


class survey_35(Page):
    form_model = 'player'
    form_fields = [
        'day_care_emergency_rearing_service_eval',
        'did_you_use_day_care_emergency_rearding_service',
    ]


class survey_36(Page):
    form_model = 'player'
    form_fields = [
        'was_day_care_emergency_rearing_service_helpful',
    ]

    def is_displayed(self):
        return self.player.did_you_use_day_care_emergency_rearding_service


class survey_37(Page):
    form_model = 'player'
    form_fields = [
        'zero_pay_linked_seoul_regional_currency_support_eval',
        'did_you_use_zero_pay_linked_seoul_regional_currency',
    ]


class survey_38(Page):
    form_model = 'player'
    form_fields = [
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
    form_model = 'player'
    form_fields = [
        'psychological_counseling_eval',
        'did_you_use_psychological_counseling',
    ]


class survey_42(Page):
    form_model = 'player'
    form_fields = [
        'was_psychological_counseling_helpful',
    ]

    def is_displayed(self):
        return self.player.did_you_use_psychological_counseling


class survey_43(Page):
    form_model = 'player'
    form_fields = [
        'H1N1_countermeasure_overall_eval',
    ]


class survey_44(Page):
    form_model = 'player'
    form_fields = [
        'H1N1_countermeasure_bad_reason',
    ]

    def is_displayed(self):
        return self.player.H1N1_countermeasure_overall_eval == 1


class survey_45(Page):
    form_model = 'player'
    form_fields = [
        'H1N1_countermeasure_good_reason',
    ]

    def is_displayed(self):
        return self.player.H1N1_countermeasure_overall_eval == 5


class survey_46(Page):
    form_model = 'player'
    form_fields = [
        'pandemic_countermeasure_govt_role_how_important',
    ]


class survey_47(Page):
    form_model = 'player'
    form_fields = [
        'pandemic_countermeasure_govt_role_not_important_why',
    ]

    def is_displayed(self):
        return self.player.pandemic_countermeasure_govt_role_how_important == 1


class survey_48(Page):
    form_model = 'player'
    form_fields = [
        'pandemic_countermeasure_govt_role_important_why',
    ]

    def is_displayed(self):
        return self.player.pandemic_countermeasure_govt_role_how_important == 5


class survey_49(Page):
    form_model = 'player'
    form_fields = [
        'emergency_cash_injection_policy_eval',
        'did_you_receive_emergency_cash_injection_policy',
    ]


class survey_50(Page):
    form_model = 'player'
    form_fields = [
        'was_emergency_cash_injection_policy_helpful',
    ]

    def is_displayed(self):
        return self.player.did_you_receive_emergency_cash_injection_policy


class survey_51(Page):
    form_model = 'player'
    form_fields = [
        'post_covid_seoul_council_policy_1',
        'post_covid_seoul_council_policy_2',
        'post_covid_seoul_council_policy_3',
        'post_covid_seoul_council_policy_1_why',
        'post_covid_seoul_council_policy_2_why',
        'post_covid_seoul_council_policy_3_why',
    ]


class survey_52(Page):
    form_model = 'player'
    form_fields = [
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


page_sequence = [survey_20, survey_21, survey_22, survey_23, survey_24, survey_25, survey_26, survey_27, survey_28,
                 survey_29, survey_30, survey_31, survey_32, survey_33, survey_34, survey_35, survey_36,
                 survey_37, survey_38, survey_39, survey_40, survey_41, survey_42, survey_43, survey_44, survey_45,
                 survey_46, survey_47, survey_48, survey_49, survey_50, survey_51, survey_52]
