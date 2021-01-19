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
    name_in_url = 'Survey'
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
    KNOWLEDGE_METRIC = GlobalConstants.KNOWLEDGE_METRIC
    seoul_council_info = survey_questions.SEOUL_COUNCIL_INFO


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def make_field_prevention_effectiveness(index):
    return models.IntegerField(
        label=Constants.prevention_effectiveness[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.COVID_EFFECTIVENESS_METRIC,
        blank=True,
    )

def make_field_prospect(index):
    return models.IntegerField(
        label=Constants.prospect[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.PROSPECT_METRIC,
        blank=True,
    )

def make_field_trust(index):
    return models.IntegerField(
        label=Constants.trust[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.TRUST_METRIC,
        blank=True,
    )
def make_field_knowledge_seoul_council(index):
    return models.IntegerField(
        label=Constants.seoul_council_info[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.KNOWLEDGE_METRIC,
        blank=True,
    )
class Player(BasePlayer):
    gender = models.IntegerField(
        label="귀하의 성별은 무엇입니까?",
        choices=[
             [0, "남성"],
             [1, "여성"],
       ],
        widget=widgets.RadioSelect,
    )
    birth_year = models.IntegerField(
        label=" 귀하의 출생년도를 선택해주십시오.",
        choices=range(2006,1949,-1),
    )
    district = models.IntegerField(
        label="귀하께서 현재 거주 중인 서울시 자치구는 어디입니까?",
        choices=[
            [1, "강남구"],
            [2, "강동구"],
            [3, "강북구"],
            [4, "강서구"],
            [5, "관악구"],
            [6, "광진구"],
            [7, "구로구"],
            [8, "금천구"],
            [9, "노원구"],
            [10, "도봉구"],
            [11, "동대문구"],
            [12, "동작구"],
            [13, "마포구"],
            [14, "서대문구"],
            [15, "서초구"],
            [16, "성동구"],
            [17, "성북구"],
            [18, "송파구"],
            [19, "양천구"],
            [20, "영등포구"],
            [21, "용산구"],
            [22, "은평구"],
            [23, "종로구"],
            [24, "중구"],
            [25, "중랑구"],
        ],
        widget=widgets.RadioSelect,
    )


    seoul_council_member_in_residential_district_knowledge = models.BooleanField(
        label = "귀하께서는 현재 거주지역의 시의원이 누구인지 알고 계십니까? (2018년 제10대 의회 기준)",
        widget = widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )
    seoul_council_member_in_residential_district_party_knowledge = models.BooleanField(
        label = "거주지역 시의원의 소속 정당명을 알고 계십니까?",
        widget = widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )
    seoul_council_in_residential_district_policy_knowledge = models.IntegerField(
        label = "귀하께서는 거주지역 시의원의 의정활동에 대해 어느 정도로 알고 계십니까?",
        widget = widgets.RadioSelect,
        choices=[
            [1, "잘 알고 있다"],
            [2, "다소 알고 있다"],
            [3, "별로 알지 못 한다"],
            [4, "전혀 알지 못 한다"],
        ],
    )

    seoul_council_member_in_residential_district_opinion = models.IntegerField(
        label="귀하께서는 서을특별시의회와 시의원들의 의정활동에 대하여 전반적으로 어떻게 생각하십니까?",
        widget = widgets.RadioSelect,
        choices = [
            [1, "매우 잘하고 있다"],
            [2, "잘하는 편이다"],
            [3, "잘못하는 편이다"],
            [4, "매우 잘못하고 있다"],
            [5, "모른다/무응답"],
        ],
    )
    seoul_council_member_in_residential_district_positive = models.IntegerField(
        label = "서울특별시의회와 시의원이 의정활동을 잘한다고 평가한 가장 큰 이유 한 가지를 간단히 서술해 주십시오.",
        choices=[
            [1, "시정 감시와 견제"],
            [2, "정책개발 및 새로운 비전 제시"],
            [3, "민생 현안 해결"],
            [4, "시민 권익증진 및 불편해소"],
            [5, "의회 청렴성 및 투명성 강화"],
            [6, "기타"],

        ],
        widget=widgets.RadioSelect,
    )
    seoul_council_member_in_residential_district_negative = models.IntegerField(
        label="서울특별시의회와 시의원이 의정활동을 잘못한다고 평가한 가장 큰 이유 한 가지를 간단히 서술해 주십시오.",
        choices=[
            [1, "시정 감시와 견제"],
            [2, "정책개발 및 새로운 비전 제시"],
            [3, "민생 현안 해결"],
            [4, "시민 권익증진 및 불편해소"],
            [5, "의회 청렴성 및 투명성 강화"],
            [6, "기타"],

        ],
        widget=widgets.RadioSelect,
    )
    COVID_infected_yesno = models.BooleanField(
        label="귀하께서는 신종 코로나바이러스에 감염된 경험이 있습니까?",
        widget = widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )
    COVID_infected_neighbors_yesno = models.BooleanField(
        label="귀하의 주변인 중 신종 코로나바이러스에 감염된 사례가 있습니까?",
        widget = widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )
    COVID_test_yesno = models.BooleanField(
        label="귀하께서는 신종 코로나바이러스 감염증 진단검사를 받은 경험이 있습니까? ",
        widget = widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )
    COVID_test_reason = models.IntegerField(
        label = "귀하께서 신종 코로나 바이러스 감염증 진단검사를 받게 된 사유에 대해 선택해주시기 바랍니다. ",
        choices=[
            [1, "해외방문"],
            [2, "신종 코로나 바이러스 확진환자와 밀접접촉"],
            [3, "코로나19 의심증상(호흡기 감염증 등) 발생"],
            [4, "입원 / 수술 목적"],
            [5, "기타"],
        ],
        widget = widgets.RadioSelect,
    )
    COVID_how_severe = models.IntegerField(
        label = "코로나19 국외 확산 상황이 얼마나 심각하다고 생각하십니까? ",
        choices=Constants.COVID_HOW_SEVERE_METRIC,
        widget = widgets.RadioSelect,
    )
    COVID_domestic_how_severe = models.IntegerField(
        label = "코로나19 국내 확산 상황이 얼마나 심각하다고 생각하십니까? ",
        choices=Constants.COVID_HOW_SEVERE_METRIC,
        widget=widgets.RadioSelect,
    )
    COVID_health_effect_how_severe = models.IntegerField(
        label="귀하께서 신종 코로나바이러스에 감염될 경우, 건강영향이나 피해가 얼마나 심각할 것 같습니까?",
        choices=Constants.COVID_HOW_SEVERE_METRIC,
        widget=widgets.RadioSelect,
    )
    COVID_financial_effect_how_severe = models.IntegerField(
        label="귀하께서 신종 코로나바이러스에 감염될 경우, 경제영향이나 피해가 얼마나 심각할 것 같습니까?",
        choices=Constants.COVID_HOW_SEVERE_METRIC,
        widget=widgets.RadioSelect,
    )
    COVID_social_effect_how_severe = models.IntegerField(
        label="귀하께서 신종 코로나바이러스에 감염될 경우, 사회영향이나 피해가 얼마나 심각할 것 같습니까?",
        choices=Constants.COVID_HOW_SEVERE_METRIC,
        widget=widgets.RadioSelect,
    )
    COVID_health_effect_experience = models.BooleanField(
        label="귀하꼐서는 신종 코로나바이러스 감염으로 인해 건강에 큰 피해를 입은 경험이 있습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    COVID_jobloss_experience = models.BooleanField(
        label="귀하께서는 신종 코로나바이러스 감염으로 인해 직업을 잃거나 폐업을 한 경험이 있습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    COVID_incomeloss_experience = models.BooleanField(
        label="귀하께서는 신종 코로나바이러스 감염으로 인해 개인소득이 감소하였습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    COVID_emotional_experience = models.BooleanField(
        label="귀하께서는 신종 코로나바이러스 감염으로 인해 극심한 스트레스 및 불안감을 느낀 경험이 있습니까? ",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    COVID_potential_infection_channel_1 = models.IntegerField(
        label="신종 코로나 바이러스의 주요 감염경로는 다음 중 무엇이라고 생각하십니까?(1순위)",
        choices=[
            [1, "가족"],
            [2, "지인"],
            [3, "대중교통"],
            [4, "다중이용시설"],
            [5, "기타"],
        ],
        widget=widgets.RadioSelect,
    )
    COVID_potential_infection_channel_2 = models.IntegerField(
        label="신종 코로나 바이러스의 주요 감염경로는 다음 중 무엇이라고 생각하십니까?(2순위)",
        choices=[
            [1, "가족"],
            [2, "지인"],
            [3, "대중교통"],
            [4, "다중이용시설"],
            [5, "기타"],
        ],
        widget=widgets.RadioSelect,
    )
    COVID_fear_which = models.IntegerField(
        label="귀하께서 만일 신종 코로나 바이러스에 감염되었다면 아래 중 어느 것에 대한 두려움이 더 크십니까? ",
        choices=[
            [1, "건강적 손실 정도(예: 감염으로 인한 건강 손실)"],
            [2, "경제적 손실 정도(예: 감염으로 인한 경제적 손실)"],
            [3, "사회적 손실 정도(예: 감염으로 인한 주변의 비난)"],
        ],
        widget=widgets.RadioSelect,
    )
    pe_1 = make_field_prevention_effectiveness(0)
    pe_2 = make_field_prevention_effectiveness(1)
    pe_3 = make_field_prevention_effectiveness(2)
    pe_4 = make_field_prevention_effectiveness(3)
    pe_5 = make_field_prevention_effectiveness(4)
    COVID_info_routinely = models.BooleanField(
        label = "귀하께서는 신종 코로나바이러스에 대한 정보를 주기적(하루에 1회 이상 직접확인)으로 얻고 있습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )
    COVID_info_source = models.IntegerField(
        label="귀하는 신종 코로나바이러스 관련정보를 다음 중 어디에서 주로 확인하는 편입니까?",
        choices=[
            [1, "포털사이트(네이버, 다음 등)"],
            [2, "대중교통내 방송(버스, 지하철 등)"],
            [3, "정기간행물(잡지 등)"],
            [4, "종이신문"],
            [5, "종편 또는 보도전문 채널(JTBC, TV조선, YTN, 연합뉴스 TV등)"],
            [6, "케이블 TV(딜라이브, 티브로드 등)"],
            [7, "지상파 방송(KBS, MBC, SBS 등)"],
            [8, "SNS(페이스북, 유튜브, 트위터, 블로그 등)"],
            [9, "라디오 방송(TBS, CBS, SBS 등)"],
            [10, "기타(지인 등)"],
            ],
        widget=widgets.RadioSelect,
    )
    COVID_info_type_1 = models.IntegerField(
        label="신종 코로나바이러스와 관련하여, 귀하께서 가장 관심 있는 정보는 무엇입니까?(1순위)",
        choices=[
            [1, "감염자현황"],
            [2, "감염원인 / 경로"],
            [3, "확진자동선"],
            [4, "감염병 영향"],
            [5, "대처방법"],
            [6, "의료기관정보"],
            [7, "기타"],
        ],
        widget=widgets.RadioSelect,
    )
    COVID_info_type_2 = models.IntegerField(
        label="신종 코로나바이러스와 관련하여, 귀하께서 가장 관심 있는 정보는 무엇입니까?(2순위)",
        choices=[
            [1, "감염자현황"],
            [2, "감염원인 / 경로"],
            [3, "확진자동선"],
            [4, "감염병 영향"],
            [5, "대처방법"],
            [6, "의료기관정보"],
            [7, "기타"],
        ],
        widget=widgets.RadioSelect,
    )
    COVID_info_enough = models.IntegerField(
        label="지금까지 접한 신종 코로나 바이러스에 대한 정보는 귀하의 궁금증을 해결하기에 충분하였습니까?",
        choices=[
            [1, "매우 부족하였다"],
            [2, "부족한 편이었다"],
            [3, "보통이다"],
            [4, "충분한 편이었다"],
            [5, "매우 충분하였다"],
        ],
        widget=widgets.RadioSelect,
    )
    COVID_termination_time = models.IntegerField(
        label="귀하께서는 신종 코로나바이러스가 국내에서 언제 종식될 것으로 예상하십니까? ",
        choices=[
            [1, "2021년 1분기(1~3월)"],
            [2, "2021년 2분기(4~6월)"],
            [3, "2021년 3분기(7~9월)"],
            [4, "2021년 4분기(10~12월) 이후"],
            [5, "1년 이내에 종식되지 않을 것 같음"],
        ],
        widget=widgets.RadioSelect,
    )
    COVID_termination_time_reason = models.IntegerField(
        label="귀하께서 위와 같이 예상하신 이유가 무엇입니까? ",
        choices=[
            [1, "코로나19 백신보급"],
            [2, "정부의 강도 높은 규제(사회적 거리두기 등) 시행"],
            [3, "민간부문에서의 기본적 방역수칙 생활화"],
            [4, "기타(직접입력)"],
        ],
        widget=widgets.RadioSelect,
    )
    COVID_termination_time_reason_op = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )
    do_you_trust_govt_prospection_for_end_of_COVID = models.IntegerField(
        label="귀하께서는 정부에서 전망하는 신종코로나 바이러스 종식 시점에 대해 어느 정도 신뢰하고 계십니까?",
        choices=[
            [1, "매우 신뢰함"],
            [2, "다소 신뢰함"],
            [3, "다소 신뢰하지 않음"],
            [4, "전혀 신뢰하지 않음"],
        ],
        widget=widgets.RadioSelect,
    )
    p1 = make_field_prospect(0)
    p2 = make_field_prospect(1)
    p3 = make_field_prospect(2)
    p4 = make_field_prospect(3)
    p5 = make_field_prospect(4)
    p6 = make_field_prospect(5)

    t1 = make_field_trust(0)
    t2 = make_field_trust(1)
    t3 = make_field_trust(2)
    t4 = make_field_trust(3)
    t5 = make_field_trust(4)
    t6 = make_field_trust(5)
    t7 = make_field_trust(6)
    COVID_countermeasure_overall_eval = models.IntegerField(
        label="귀하께서는 정부가 신종 코로나 바이러스 사태에 대해 대응을 어떻게 하고 있다고 생각하십니까?",
        choices=[
            [1, "매우 잘하고 있다"],
            [2, "대체로 잘하고 있다"],
            [3, "대체로 못하고 있다"],
            [4, "매우 못하고 있다"],
            [5, "잘 모르겠다"],
        ],
        widget=widgets.RadioSelect,
    )
    COVID_countermeasure_welldone_reason = models.IntegerField(
        label="귀하께서 정부가 신종 코로나 바이러스 사태에 대해 대응을 잘하고 있다고 평가한 이유가 무엇인지 간단하게 서술해 주십시오.",
        choices=[
            [1, "사회적 거리두기 규제"],
            [2, "긴급재난지원금 제공"],
            [3, "원격수업 관련 인프라 지원"],
            [4, "지원아이돌봄서비스 지원(행정절차 간소화)"],
            [5, "코로나19 대응 교육현장 부담완화(교육인력지원 및 행정면책 추진)"],
        ],
        widget=widgets.RadioSelect,
    )
    COVID_countermeasure_wrongdoing_reason = models.StringField(
        label="귀하께서 정부가 신종 코로나 바이러스 사태에 대해 대응을 잘못하고 있다고 평가한 이유가 무엇인지 간단하게 서술해 주십시오.",
    )
    COVID_policy_info_source = models.IntegerField(
        label="귀하께서는 정부가 신종 코로나바이러스 감염확산에 대응하기 위해 시행 중인 정책에 관련된 정보를 주로 어디서 확인하십니까?",
        choices=[
            [1, "포털사이트(네이버, 다음 등)"],
            [2, "대중교통내 방송(버스, 지하철 등)"],
            [3, "정기간행물(잡지 등)"],
            [4, "종이신문"],
            [5, "종편 또는 보도전문 채널(JTBC, TV조선, YTN, 연합뉴스 TV등)"],
            [6, "케이블 TV(딜라이브, 티브로드 등)"],
            [7, "지상파 방송(KBS, MBC, SBS 등)"],
            [8, "SNS(페이스북, 유튜브, 트위터, 블로그 등)"],
            [9, "라디오 방송(TBS, CBS, SBS 등)"],
            [10, "기타(지인 등)"],
        ],
        widget=widgets.RadioSelect,
    )
    COVID_countermeasure_social_distancing_evaluation = models.IntegerField(
        label="귀하께서는 코로나 19확산을 막기위해 정부에서 시행 중인 사회적 거리두기 정책에 대해 어떻게 생각하십니까?",
        choices=[
            [1, "매우 지나치다"],
            [2, "다소 지나치다"],
            [3, "적절하다"],
            [4, "다소 부족하다"],
            [5, "매우 부족하다"],
        ],
        widget=widgets.RadioSelect,
    )
    social_distancing_overreaction = models.IntegerField(
        label="현재 시행 중인 사회적 거리두기 방역수칙(2020.12.7.기준) 중 지나치다고 생각하는 영역은 무엇입니까?",
        choices=[
            [1, "다중이용시설 방역조치 위반시 원스트라이크 아웃제"],
            [2, "중점관리시설(유흥시설, 공연장, 노래연습장, 홍보관 등) 집합금지"],
            [3, "중점관리시설(식당‧카페) 마스크 착용, 출입자 명단관리, 환기‧소독 의무화"],
            [4, "중점관리시설(식당‧카페) 포장‧배달만 허용(식당은21시 이후부터)"],
            [5, "일반관리시설 집합금지 및 21시 익일 05시 까지 운영 중단"],
            [6, "일반관리시설 인원제한, 음식 섭취 금지, 좌석 띄우기"],
            [7, "기타(직접입력)"],
        ],
        widget=widgets.RadioSelect,
    )
    social_distancing_overreaction_op = models.StringField(
       label="기타(직접입력)",
        blank=True,
    )
    social_distancing_underreaction = models.IntegerField(
        label="현재 시행 중인 사회적 거리두기 방역수칙(2020.12.7.기준) 중 부족하다고 생각하는 영역은 무엇입니까?",
        choices=[
            [1, "다중이용시설 방역조치 위반시 원스트라이크 아웃제"],
            [2, "중점관리시설(유흥시설, 공연장, 노래연습장, 홍보관 등) 집합금지"],
            [3, "중점관리시설(식당‧카페) 마스크 착용, 출입자 명단관리, 환기‧소독 의무화"],
            [4, "중점관리시설(식당‧카페) 포장‧배달만 허용(식당은21시 이후부터)"],
            [5, "일반관리시설 집합금지 및 21시 익일 05시 까지 운영 중단"],
            [6, "일반관리시설 인원제한, 음식 섭취 금지, 좌석 띄우기"],
            [7, "기타(직접입력)"],
        ],
        widget=widgets.RadioSelect,
    )
    social_distancing_underreaction_op = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )
    ksc1 = make_field_knowledge_seoul_council(0)
    ksc2 = make_field_knowledge_seoul_council(1)
    ksc3 = make_field_knowledge_seoul_council(2)
    ksc4 = make_field_knowledge_seoul_council(3)
    ksc5 = make_field_knowledge_seoul_council(4)
    ksc6 = make_field_knowledge_seoul_council(5)
    ksc7 = make_field_knowledge_seoul_council(6)
    ksc8 = make_field_knowledge_seoul_council(7)
    ksc9 = make_field_knowledge_seoul_council(8)
    ksc10 = make_field_knowledge_seoul_council(9)
    ksc11 = make_field_knowledge_seoul_council(10)
    ksc12 = make_field_knowledge_seoul_council(11)

    seoul_council_budget_yesno = models.IntegerField(
        label = "서울시의회 예산이 어느정도인가 아시는가?",
        widget = widgets.RadioSelect,
        choices = range(10,110,10),
    )
    seoul_council_record_available = models.BooleanField(
        label = "서울시의회 회의 자료가 공개되어 있는 것을 아시는가?",
        widget = widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )