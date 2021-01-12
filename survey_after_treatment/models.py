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
from . import survey_questions
#import numpy as np
author = 'Kyubum Moon<mailto:moonx190@umn.edu> & Namun Cho'

doc = """
행동경제학적 관점에서 본 포스트 코로나 시대의 서울시의회의 역할과 과제
"""


class Constants(BaseConstants):
    name_in_url = 'survey_after_treatment'
    players_per_group = None
    num_rounds = 1
    BINARY_CHOICES = GlobalConstants.BINARY_CHOICES
    prevention_effectiveness = survey_questions.PREVENTION_EFFECTIVENESS
    COVID_HOW_SEVERE_METRIC = [
        [1, "전혀 심각하지 않다"],
        [2, "심각하지 않은 편이다"],
        [3, "보통이다"],
        [4, "심각한 편이다"],
        [5, "매우 심각하다 "],
    ]
    COVID_EFFECTIVENESS_METRIC = GlobalConstants.COVID_EFFECTIVENESS_METRIC
    PROSPECT_METRIC = GlobalConstants.PROSPECT_METRIC
    prospect = survey_questions.PROSPECT_OUTLOOK
    TRUST_METRIC = GlobalConstants.TRUST_METRIC
    trust = survey_questions.TRUST_TARGET

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    seoul_council_trust_metric = models.IntegerField(
        label="서울시의회에 대한 귀하의 신뢰 정도를 선택해주십시오.",
        choices=[
            [1, "전혀신뢰하지않는다"],
            [2, "약간신뢰하지않는다"],
            [3, "중간이다"],
            [4, "약간 신뢰한다"],
            [5, "매우 신뢰한다"],
        ],
        widget=widgets.RadioSelect,
    )
    seoul_council_policy_support_metric = models.IntegerField(
        label="서울시의회가 현재 수행하고 있는 정책 전반에 대한 귀하의 지지 정도를 선택해주십시오.",
        choices=[
            [1, "매우 반대한다"],
            [2, "약간 반대한다"],
            [3, "중간이다"],
            [4, "약간 지지한다"],
            [5, "매우 지지한다"],
        ],
        widget=widgets.RadioSelect,
    )
    emergency_cash_injection_evaluation = models.IntegerField(
        label="2020년 실시된 서울시 재난긴급생활비 지원 정책을 어떻게 평가 하십니까?",
        choices=[
            [1, "매우 부정적이다"],
            [2, "약간 부정적이다"],
            [3, "중간이다"],
            [4, "약간 긍정적이다"],
            [5, "매우 긍정적이다"],
        ],
        widget=widgets.RadioSelect,
    )
    did_you_receive_emergency_cash_injection = models.BooleanField(
        label="2020년 서울시 재난긴급생활지원비를 받으셨습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    was_emergency_cash_injection_helpful = models.IntegerField(
        label="코로나19로 인해 귀하가 받은 피해나 생활의 변화를 개선하는 데 서울시 재난긴급생활비 지원 정책이 얼마나 도움이 되었습니까?",
        choices=[
            [1, "전혀 도움되지 않았다"],
            [2, "약간 도움되지 않았다"],
            [3, "중간이다"],
            [4, "약간 도움되었다"],
            [5, "매우 도움되었다"],
        ],
        widget=widgets.RadioSelect,
    )
    after_nine_transportation_control_eval = models.IntegerField(
        label="사회적 거리두기 비상조치의 일환으로 지난달 2020년 12월을 지칭 (조사실시를 2021년 1월로 가정함)부터 실시하고 있는 서울시 저녁 9시 이후 대중교통 감축운행 정책을 어떻게 평가하십니까?",
        choices=[
            [1, "매우 부정적이다"],
            [2, "약간 부정적이다"],
            [3, "중간이다"],
            [4, "약간 긍정적이다"],
            [5, "매우 긍정적이다"],
        ],
        widget=widgets.RadioSelect,
    )
    after_nine_transportation_control_experience_yesno = models.BooleanField(
        label="서울시 저녁 9시 이후 대중교통 감축운행 정책 실시 이후 서울시 대중교통을 이용해본 적 있으십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    after_nine_transportation_control_helpful_metric = models.IntegerField(
        label="코로나19로 인해 귀하가 받은 피해나 생활의 변화를 개선하는 데 서울시 저녁 9시 이후 대중교통 감축운행 정책이 얼마나 도움이 되었습니까?",
        choices=[
            [1, "전혀 도움되지 않았다"],
            [2, "약간 도움되지 않았다"],
            [3, "중간이다"],
            [4, "약간 도움되었다"],
            [5, "매우 도움되었다"],
        ],
        widget=widgets.RadioSelect,
    )
    crisis_emergency_support_eval = models.IntegerField(
        label="2020년 실시된 서울시 위기가구 긴급생계지원 정책을 어떻게 평가하십니까? ",
        choices=[
            [1, "매우 부정적이다"],
            [2, "약간 부정적이다"],
            [3, "중간이다"],
            [4, "약간 긍정적이다"],
            [5, "매우 긍정적이다"],
        ],
        widget=widgets.RadioSelect,
    )
    did_you_receive_crisis_emergency_support = models.BooleanField(
        label="2020년 서울시 위기가구 긴급생계지원비를 받으셨습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    was_crisis_emergency_support_helpful = models.IntegerField(
        label="코로나19로 인해 귀하가 받은 피해나 생활의 변화를 개선하는 데 서울시 위기가구 긴급생계지원 정책이 얼마나 도움이 되었습니까?",
        choices=[
            [1, "전혀 도움되지 않았다"],
            [2, "약간 도움되지 않았다"],
            [3, "중간이다"],
            [4, "약간 도움되었다"],
            [5, "매우 도움되었다"],
        ],
        widget=widgets.RadioSelect,
    )
    seoul_student_food_stamp_eval = models.IntegerField(
        label="2020년 실시된 서울시 학생 식재료 꾸러미 지원 정책을 어떻게 평가하십니까?",
        choices=[
            [1, "매우 부정적이다"],
            [2, "약간 부정적이다"],
            [3, "중간이다"],
            [4, "약간 긍정적이다"],
            [5, "매우 긍정적이다"],
        ],
        widget=widgets.RadioSelect,
    )
    did_you_receive_food_stamp = models.BooleanField(
        label="2020년 서울시 학생 식재료 꾸러미 바우처를 받으셨습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    was_food_stamp_helpful = models.IntegerField(
        label="코로나19로 인해 귀하가 받은 피해나 생활의 변화를 개선하는 데 서울시 학생 식재료 꾸러미 지원 정책이 얼마나 도움이 되었습니까?",
        choices=[
            [1, "전혀 도움되지 않았다"],
            [2, "약간 도움되지 않았다"],
            [3, "중간이다"],
            [4, "약간 도움되었다"],
            [5, "매우 도움되었다"],
        ],
        widget=widgets.RadioSelect,
    )
    free_online_learning_eval = models.IntegerField(
        label="2020년 실시된 서울시 무료 온라인 학습강좌 확대 정책을 어떻게 평가하십니까?",
        choices=[
            [1, "매우 부정적이다"],
            [2, "약간 부정적이다"],
            [3, "중간이다"],
            [4, "약간 긍정적이다"],
            [5, "매우 긍정적이다"],
        ],
        widget=widgets.RadioSelect,
    )
    did_you_use_free_online_learning = models.BooleanField(
        label="2020년 실시된 서울시 무료 온라인 학습강좌 확대 이후 서울시 무료 온라인 학습강좌를 사용해보셨습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    was_free_online_learning_helpful = models.IntegerField(
        label="코로나19로 인해 귀하가 받은 피해나 생활의 변화를 개선하는 데 서울시 무료 온라인 학습강좌 확대 정책이 얼마나 도움이 되었습니까?",
        choices=[
            [1, "전혀 도움되지 않았다"],
            [2, "약간 도움되지 않았다"],
            [3, "중간이다"],
            [4, "약간 도움되었다"],
            [5, "매우 도움되었다"],
        ],
        widget=widgets.RadioSelect,
    )
    emergency_day_care_eval = models.IntegerField(
        label="2020년 실시된 서울시 유아 및 초등학생 대상 긴급돌봄교실 운영 정책을 어떻게 평가하십니까?",
        choices=[
            [1, "매우 부정적이다"],
            [2, "약간 부정적이다"],
            [3, "중간이다"],
            [4, "약간 긍정적이다"],
            [5, "매우 긍정적이다"],
        ],
        widget=widgets.RadioSelect,
    )
    did_you_use_emergency_day_care = models.BooleanField(
        label="2020년 서울시 유아 및 초등학생 대상 긴급돌봄교실을 이용해본 적 있으십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    was_emergency_day_care_helpful = models.IntegerField(
        label="2020년 서울시 유아 및 초등학생 대상 긴급돌봄교실이 얼마나 도움이 되었습니까?",
        choices=[
            [1, "전혀 도움되지 않았다"],
            [2, "약간 도움되지 않았다"],
            [3, "중간이다"],
            [4, "약간 도움되었다"],
            [5, "매우 도움되었다"],
        ],
        widget=widgets.RadioSelect,
    )
    weak_people_emergency_care_eval = models.IntegerField(
        label="2020년 실시된 서울시 어르신 및 장애인 대상 긴급돌봄서비스 정책을 어떻게 평가하십니까?",
        choices=[
            [1, "매우 부정적이다"],
            [2, "약간 부정적이다"],
            [3, "중간이다"],
            [4, "약간 긍정적이다"],
            [5, "매우 긍정적이다"],
        ],
        widget=widgets.RadioSelect,
    )
    did_you_use_weak_people_emergency_care = models.BooleanField(
        label="2020년 서울시 어르신 및 장애인 대상 긴급돌봄서비스를 이용해본 적 있으십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    was_weak_people_emergency_care_helpful = models.IntegerField(
        label="코로나19로 인해 귀하가 받은 피해나 생활의 변화를 개선하는 데 서울시 어르신 및 장애인 대상 긴급돌봄서비스 정책이 얼마나 도움이 되었습니까?",
        choices=[
            [1, "전혀 도움되지 않았다"],
            [2, "약간 도움되지 않았다"],
            [3, "중간이다"],
            [4, "약간 도움되었다"],
            [5, "매우 도움되었다"],
        ],
        widget=widgets.RadioSelect,
    )
    day_care_emergency_rearing_service_eval = models.IntegerField(
        label="2020년 실시된 서울시 어린이집 긴급보육서비스 운영 정책을 어떻게 평가하십니까?",
        choices=[
            [1, "매우 부정적이다"],
            [2, "약간 부정적이다"],
            [3, "중간이다"],
            [4, "약간 긍정적이다"],
            [5, "매우 긍정적이다"],
        ],
        widget=widgets.RadioSelect,
    )
    did_you_use_day_care_emergency_rearding_service = models.BooleanField(
        label="2020년 서울시 어린이집 긴급보육서비스를 이용해본 적 있으십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    was_day_care_emergency_rearing_service_helpful = models.IntegerField(
        label="코로나19로 인해 귀하가 받은 피해나 생활의 변화를 개선하는 데 서울시 어린이집 긴급보육서비스 운영 정책이 얼마나 도움이 되었습니까?",
        choices=[
            [1, "전혀 도움되지 않았다"],
            [2, "약간 도움되지 않았다"],
            [3, "중간이다"],
            [4, "약간 도움되었다"],
            [5, "매우 도움되었다"],
        ],
        widget=widgets.RadioSelect,
    )
    zero_pay_linked_seoul_regional_currency_support_eval = models.IntegerField(
        label="2020년 실시된 서울시 제로페이 연계 서울사랑상품권 소비자혜택 한시적 상향 조정 정책을 어떻게 평가하십니까?",
        choices=[
            [1, "매우 부정적이다"],
            [2, "약간 부정적이다"],
            [3, "중간이다"],
            [4, "약간 긍정적이다"],
            [5, "매우 긍정적이다"],
        ],
        widget=widgets.RadioSelect,
    )
    did_you_use_zero_pay_linked_seoul_regional_currency = models.BooleanField(
        label="2020년 해당 기간 동안 서울시 제로페이 연계 서울사랑상품권을 이용해본 적 있으십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    was_zero_pay_linked_seoul_regional_currency_helpful = models.IntegerField(
        label="코로나19로 인해 귀하가 받은 피해나 생활의 변화를 개선하는 데 서울시 제로페이 연계 서울사랑상품권 소비자혜택 한시적 상향 조정 정책이 얼마나 도움이 되었습니까?",
        choices=[
            [1, "전혀 도움되지 않았다"],
            [2, "약간 도움되지 않았다"],
            [3, "중간이다"],
            [4, "약간 도움되었다"],
            [5, "매우 도움되었다"],
        ],
        widget=widgets.RadioSelect,
    )
    special_worker_free_lancer_support_eval = models.IntegerField(
        label="2020년 실시된 서울시 특수고용노동자 및 프리랜서 특별지원 정책을 어떻게 평가하십니까?",
        choices=[
            [1, "매우 부정적이다"],
            [2, "약간 부정적이다"],
            [3, "중간이다"],
            [4, "약간 긍정적이다"],
            [5, "매우 긍정적이다"],
        ],
        widget=widgets.RadioSelect,
    )
    did_you_receive_special_worker_free_lancer_support = models.BooleanField(
        label="2020년 서울시 특수고용노동자 및 프리랜서 특별지원금을 받으셨습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    was_special_worker_free_lancer_support_helpful = models.IntegerField(
        label="코로나19로 인해 귀하가 받은 피해나 생활의 변화를 개선하는 데 서울시 특수고용노동자 및 프리랜서 특별지원 정책이 얼마나 도움이 되었습니까?",
        choices=[
            [1, "전혀 도움되지 않았다"],
            [2, "약간 도움되지 않았다"],
            [3, "중간이다"],
            [4, "약간 도움되었다"],
            [5, "매우 도움되었다"],
        ],
        widget=widgets.RadioSelect,
    )
    psychological_counseling_eval = models.IntegerField(
        label="2020년 실시된 서울시 코로나19 피해 노동자 ‘스트레스·불안 해소 심리상담’ 서비스 정책을 어떻게 평가하십니까?",
        choices=[
            [1, "매우 부정적이다"],
            [2, "약간 부정적이다"],
            [3, "중간이다"],
            [4, "약간 긍정적이다"],
            [5, "매우 긍정적이다"],
        ],
        widget=widgets.RadioSelect,
    )
    did_you_use_psychological_counseling = models.BooleanField(
        label="2020년 서울시 코로나19 피해 노동자 ‘스트레스·불안 해소 심리상담’ 서비스를 이용해본 적 있으십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    was_psychological_counseling_helpful = models.IntegerField(
        label="코로나19로 인해 귀하가 받은 피해나 생활의 변화를 개선하는 데 서울시 코로나19 피해 노동자 ‘스트레스·불안 	해소 심리상담’ 서비스 정책이 얼마나 도움이 되었습니까?",
        choices=[
            [1, "전혀 도움되지 않았다"],
            [2, "약간 도움되지 않았다"],
            [3, "중간이다"],
            [4, "약간 도움되었다"],
            [5, "매우 도움되었다"],
        ],
        widget=widgets.RadioSelect,
    )
    H1N1_countermeasure_overall_eval = models.IntegerField(
        label="코로나19 이전 발생했던 범유행전염병인 신종플루 유행 상황에 대응하기 위한 서울특별시의회의 정책적 방안에 대해 전반적으로 어떻게 평가하시겠습니까?",
        choices=[
            [1, "전혀 적절치 못하게 대응했다"],
            [2, "약간 적절치 못하게 대응했다"],
            [3, "중간이다"],
            [4, "약간 적절하게 대응했다"],
            [5, "매우 적절하게 대응했다"],
            [6, "당시 서울특별시의회의 대응방식에 대해 알지 못한다"],
        ],
        widget=widgets.RadioSelect,
    )
    H1N1_countermeasure_bad_reason = models.StringField(
        label="2009년 신종플루 유행 당시 서울시의회가 ‘전혀 적절치 못하게 대응했다’고 평가하신 이유는 무엇입니까?",
    )
    H1N1_countermeasure_good_reason = models.StringField(
        label="2009년 신종플루 유행 당시 서울시의회가 ‘매우 적절하게 대응했다’고 평가하신 이유는 무엇입니까?",
    )
    pandemic_countermeasure_govt_role_how_important = models.IntegerField(
        label="범유행전염병에 대응하기 위해서 정부의 역할이 얼마나 중요하	다고 보십니까?",
        choices=[
            [1, "전혀 중요하지 않다"],
            [2, "약간 중요하지 않다"],
            [3, "중간이다"],
            [4, "약간 중요하다"],
            [5, "매우 중요하다"],
        ],
        widget=widgets.RadioSelect,
    )
    pandemic_countermeasure_govt_role_not_important_why = models.StringField(
        label="범유행전염병 대응과정에서 정부의 역할이 ‘전혀 중요하지 않다’고 응답하신 이유는 무엇입니까?",
    )
    pandemic_countermeasure_govt_role_important_why = models.StringField(
        label="범유행전염병 대응과정에서 정부의 역할이 ‘매우 중요하다’고 응답하신 이유는 무엇입니까?",
    )
    emergency_cash_injection_policy_eval = models.IntegerField(
        label="2020년 실시된 정부 긴급재난지원금 지급 정책을 어떻게 평가	하십니까? ",
        choices=[
            [1, "매우 부정적이다"],
            [2, "약간 부정적이다"],
            [3, "중간이다"],
            [4, "약간 긍정적이다"],
            [5, "매우 긍정적이다"],
        ],
        widget=widgets.RadioSelect,
    )
    did_you_receive_emergency_cash_injection_policy = models.BooleanField(
        label="2020년 정부 긴급재난지원금을 받으셨습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    was_emergency_cash_injection_policy_helpful = models.IntegerField(
        label="코로나19로 인해 귀하가 받은 피해나 생활의 변화를 개선하는 데 정부 긴급재난지원금 지급 정책이 얼마나 도움이 되었습니까?",
        choices=[
            [1, "전혀 도움되지 않았다"],
            [2,  "약간 도움되지 않았다"],
            [3,  "중간이다"],
            [4,  "약간 도움되었다"],
            [5,  "매우 도움되었다"],
        ],
        widget=widgets.RadioSelect,
    )
    post_covid_seoul_council_policy_1 = models.IntegerField(
        label="포스트코로나 시대에는 다음 중 어떤 분야에 서울시의회가 정책 역량을 집중해야 한다고 보십니까? 귀하가 생각하시기에 중요한 순서대로 3가지 우선순위를 선택해주세요.(1순위)",
        choices=[
            [1,"행정자치"],
            [2, "보건복지"],
            [3, "도시계획"],
            [4, "지방경제"],
            [5, "교통"],
            [6, "교육"],
            [7, "문화체육"],
            [8, "환경"],
        ],
        widget=widgets.RadioSelect,
    )
    post_covid_seoul_council_policy_2 = models.IntegerField(
        label="포스트코로나 시대에는 다음 중 어떤 분야에 서울시의회가 정책 역량을 집중해야 한다고 보십니까? 귀하가 생각하시기에 중요한 순서	대로 3가지 우선순위를 선택해주세요.(2순위)",
        choices=[
            [1, "행정자치"],
            [2, "보건복지"],
            [3, "도시계획"],
            [4, "지방경제"],
            [5, "교통"],
            [6, "교육"],
            [7, "문화체육"],
            [8, "환경"],
        ],
        widget=widgets.RadioSelect,
    )
    post_covid_seoul_council_policy_3 = models.IntegerField(
        label="포스트코로나 시대에는 다음 중 어떤 분야에 서울시의회가 정책 역량을 집중해야 한다고 보십니까? 귀하가 생각하시기에 중요한 순서	대로 3가지 우선순위를 선택해주세요.(3순위)",
        choices=[
            [1, "행정자치"],
            [2, "보건복지"],
            [3, "도시계획"],
            [4, "지방경제"],
            [5, "교통"],
            [6, "교육"],
            [7, "문화체육"],
            [8, "환경"],
        ],
        widget=widgets.RadioSelect,
    )
    post_covid_seoul_council_policy_1_why = models.StringField(
        label="1순위로 선택하신 분야를 1순위로 선택하신 이유는 무엇입니까?",
    )
    post_covid_seoul_council_policy_2_why = models.StringField(
        label="2순위로 선택하신 분야를 2순위로 선택하신 이유는 무엇입니까?",
    )
    post_covid_seoul_council_policy_3_why = models.StringField(
        label="3순위로 선택하신 분야를 3순위로 선택하신 이유는 무엇입니까?",
    )
    when_did_you_move_to_the_district_year = models.IntegerField(
        label="해당 자치구로 이전해오신 년도는 어떻게 되십니까?",
        choices=range(2020, 1949,-1),
    )
    when_did_you_move_to_the_district_month = models.IntegerField(
        label="몇월에 해당자치구로 이전해오셨습니까?",
        choices=range(1, 13),
    )
    where_did_you_reside_2016 = models.StringField(
        label="2016년에 거주했던 지역을 작성해주세요. (구, 군단위까지)",
    )
    where_did_you_reside_2017 = models.StringField(

        label="2017년에 거주했던 지역을 작성해주세요. (구, 군단위까지)",
    )
    where_did_you_reside_2018 = models.StringField(

        label="2018년에 거주했던 지역을 작성해주세요. (구, 군단위까지)",
    )
    where_did_you_reside_2019 = models.StringField(

        label="2019년에 거주했던 지역을 작성해주세요. (구, 군단위까지)",
    )
    where_did_you_reside_2020 = models.StringField(

        label="2020년에 거주했던 지역을 작성해주세요. (구, 군단위까지)",
    )
    household_income = models.IntegerField(
        label="최근 6개월 평균 가구소득액(즉, 가족 구성원 전체의 수입 합산액)은 어떻게 되십니까? 월별 세후 수령액 기준으로 선택해 주십시오.",
        choices=[
            [1, "없음"],
            [2, "150만원 미만"],
            [3, "150만원 이상 300만원 미만"],
            [4, "300만원 이상 450만원 미만"],
            [5, "450만원 이상 600만원 미만"],
            [6, "600만원 이상 750만원 미만"],
            [7, "750만원 이상"],
        ],
        widget=widgets.RadioSelect,
    )
    high_class_standard = models.IntegerField(
        label="귀하께서는 소득과 자산 총액을 기준으로 대한민국 국민을 일렬로 세웠을 때 상위 어느 정도 이내가 상류층이라고 보십니까? 상류층 : 상위    % 이내",
        choices=range(1,100),
    )
    middle_class_standard = models.IntegerField(
        label="귀하께서는 소득과 자산 총액을 기준으로 대한민국 국민을 일렬로 세웠을 때 상위 어느 정도 이내가 중산층이라고 보십니까? 중산층 : 상위    % 이내",
        choices=range(1, 100),

    )
    occupation = models.IntegerField(
        label="귀하께서 현재 근무하시는 기업의 업종은 다음 중 무엇입니까? 최근 1년 이내 근무경험 없으면 10)을 선택해주세요.",
        choices=[
            [1, "제조업"],
            [2, "보건업 및 사회복지 서비스업"],
            [3, "도매 및 소매업"],
            [4, "숙박 및 음식점업"],
            [5, "전문, 과학 및 기술서비스업"],
            [6, "교육 서비스업"],
            [7, "정보통신업"],
            [8, "기타"],
            [9, "모르겠음"],
            [10, "최근 1 년 이내 근무경험 없음"],
        ],
        widget=widgets.RadioSelect,
    )
    special_worker_or_freelancer = models.BooleanField(
        label=" 귀하는 특수고용노동자 또는 프리랜서입니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    final_schooling = models.IntegerField(
        label="귀하의 최종 학력을 선택해주세요",
        choices=[
            [1, "고등학교 졸업 이하"],
            [2, "(2·3년제) 전문대학 졸업"],
            [3, "4 년제 대학교 졸업"],
            [4, "대학원 졸업 이상"],
        ],
        widget=widgets.RadioSelect,
    )
    health_state = models.IntegerField(
        label="귀하 자신이 평가하는 건강상태는 어떠십니까?",
        choices=[
            [1, "매우 나쁘다"],
            [2, "약간 나쁘다"],
            [3, "보통이다"],
            [4, "약간 건강하다"],
            [5, "매우 건강하다"],
        ],
        widget=widgets.RadioSelect,
    )
    voted = models.BooleanField(
        label="귀하는 2020년 제21대 국회의원선거(4월 15일 실시)에 참여하셨습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    political_inclination = models.IntegerField(
        label="귀하는 자신의 정치적 성향을 다음 중 어디에 가장 가깝다고 생각하십니까?",
        choices=[
            [1, "진보(좌파)"],
            [2, "온건 진보(중도좌파)"],
            [3, "중도"],
            [4, "중도 보수(중도우파)"],
            [5, "보수(우파)"],
        ],
        widget=widgets.RadioSelect,
    )
