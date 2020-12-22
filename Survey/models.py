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

author = 'Kyubum Moon<mailto:moonx190@umn.edu> & Namun Cho'

doc = """
행동경제학적 관점에서 본 포스트 코로나 시대의 서울시의회의 역할과 과제
"""


class Constants(BaseConstants):
    name_in_url = 'Survey'
    players_per_group = None
    num_rounds = 1
    BINARY_CHOICES = GlobalConstants.BINARY_CHOICES


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    seoul_council_member_in_residential_district_knowledge = models.BooleanField(
        label = "귀하께서는 현재 거주지역의 시의원이 누구인지 알고 계십니까? (2018년 제10대 의회 기준) (자체제작)",
        widget = widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )
    seoul_council_member_in_residential_district_party_knowledge = models.BooleanField(
        label = "거주지역 시의원의 소속 정당명을 알고 계십니까? (자체제작)",
        widget = widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )
    seoul_council_in_residential_district_policy_knowledge = models.IntegerField(
        label = "귀하께서는 거주지역 시의원의 의정활동에 대해 어느 정도로 알고 계십니까? (자체제작)",
        widget = widgets.RadioSelect,
        choices=[
            [1, "잘 알고 있다"],
            [2, "다소 알고 있다"],
            [3, "별로 알지 못 한다"],
            [4, "전혀 알지 못 한다"],
        ],
    )
    seoul_council_in_residential_district_channel = models.IntegerField(
        label = "귀하께서 서울시의회나 시의원 관련 홍보, 언론보도 및 소식을 가장 자주 접하는 매체는 무엇입니까? (복수응답가능)  (출처 : 리얼미터)",
        widget = widgets.RadioSelect,
        choices=[
            [1, "포털사이트(네이버, 다음 등)"],
            [2, "대중교통내 방송(버스, 지하철 등)"],
            [3, "정기간행물(의회 소식지, 잡지 등)"],
            [4, "종이신문"],
            [5, "종편 또는 보도전문 채널(JTBC, TV조선, YTN, 연합뉴스 TV등)"],
            [6, "케이블 TV(딜라이브, 티브로드 등)"],
            [7, "지상파 방송(KBS, MBC, SBS 등)"],
            [8, "SNS(페이스북, 유튜브, 트위터, 블로그 등)"],
            [9, "라디오 방송(TBS, CBS, SBS 등)"],
            [10, "기타(지인 등)"],
            [11, "해당없음(미인식)"],

        ]
    )
    seoul_council_member_in_residential_district_opinion = models.IntegerField(
        label="귀하께서는 서을특별시의회와 시의원들의 의정활동에 대하여 전반적으로 어떻게 생각하십니까? (출처 : 리얼미터)",
        widget = widgets.RadioSelect,
        choices = [
            [1, "매우 잘하고 있다 (Q6으로 이동)"],
            [2, "잘하는 편이다 (Q6으로 이동)"],
            [3, "잘못하는 편이다 (Q7로 이동)"],
            [4, "매우 잘못하고 있다 (Q7로 이동)"],
            [5, "모른다/무응답"],
        ],
    )
    seoul_council_member_in_residential_district_positive = models.StringField(
        label = "(Q5 1 또는 2 응답자만) 서울특별시의회와 시의원이 의정활동을 잘한다고 평가한 가장 큰 이유 한 가지를 간단히 서술해 주십시오. (Q8로 이동) (자체제작)",
        blank=True,
    )
    seoul_council_member_in_residential_district_negative = models.StringField(
        label=" (Q5 3 또는 4 응답자만) 서울특별시의회와 시의원이 의정활동을 잘못한다고 평가한 가장 큰 이유 한 가지를 간단히 서술해 주십시오. ((Q8로 이동) (자체제작)",
        blank = True,
    )
