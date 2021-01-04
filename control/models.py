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

author = 'Kyubum Moon'

doc = """
행동경제학 관점에서 본 포스트 코로나 시대의 서울시의회의 역할과 과제
"""


class Constants(BaseConstants):
    name_in_url = 'control'
    players_per_group = None
    num_rounds = 1
    DISTRICTS = [
        [1, '강남구'],
        [2, '강동구'],
        [3, '강북구'],
        [4, '강서구'],
        [5, '관악구'],
        [6, '광진구'],
        [7, '구로구'],
        [8, '금천구'],
        [9, '노원구'],
        [10, '도봉구'],
        [11, '동대문구'],
        [12, '동작구'],
        [13, '마포구'],
        [14, '서대문구'],
        [15, '서초구'],
        [16, '성동구'],
        [17, '성북구'],
        [18, '송파구'],
        [19, '양천구'],
        [20, '영등포구'],
        [21, '용산구'],
        [22, '은평구'],
        [23, '종로구'],
        [24, '중구'],
        [25, '중랑구'],
    ]

    GU_DONG_MAP = GlobalConstants.GU_DONG_MAP
    GU_INDEX = GlobalConstants.GU_INDEX
    INDEX_GU = GlobalConstants.INDEX_GU
    KEY_COUNCIL_NUMER = GlobalConstants.KEY_COUNCIL_NUMER
    INDEX_GU_KOR = GlobalConstants.INDEX_GU_KOR

    WAITING_SECONDS = GlobalConstants.WAITING_SECONDS


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def make_gu_field(gu):
    return models.IntegerField(
        choices=Constants.GU_DONG_MAP[gu],
        label="귀하의 거주구역을 선택해주십시오.",
        widget=widgets.RadioSelect,
    )


class Player(BasePlayer):
    districts = models.IntegerField(
        label = "귀하의 지역구를 선택해주십시오.",
        choices = Constants.DISTRICTS,
        widget = widgets.RadioSelect,
    )

    gangnam_gu = make_gu_field("gangnam_gu")
    gangdong_gu = make_gu_field("gangdong_gu")
    gangbuk_gu = make_gu_field("gangbuk_gu")
    gangseo_gu = make_gu_field("gangseo_gu")
    gwanak_gu = make_gu_field("gwanak_gu")
    gwangjin_gu = make_gu_field("gwangjin_gu")
    guro_gu = make_gu_field("guro_gu")
    geumcheon_gu = make_gu_field("geumcheon_gu")
    nowon_gu = make_gu_field("nowon_gu")
    dobong_gu = make_gu_field("dobong_gu")
    dongdaemun_gu = make_gu_field("dongdaemun_gu")
    dongjak_gu = make_gu_field("dongjak_gu")
    mapo_gu = make_gu_field("mapo_gu")
    seodaemun_gu = make_gu_field("seodaemun_gu")
    seocho_gu = make_gu_field("seocho_gu")
    seongdong_gu = make_gu_field("seongdong_gu")
    seongbuk_gu = make_gu_field("seongbuk_gu")
    songpa_gu = make_gu_field("songpa_gu")
    yangcheon_gu = make_gu_field("yangcheon_gu")
    yeongdeungpo_gu = make_gu_field("yeongdeungpo_gu")
    yongsan_gu = make_gu_field("yongsan_gu")
    eunpyung_gu = make_gu_field("eunpyung_gu")
    jongro_gu = make_gu_field("jongro_gu")
    jung_gu = make_gu_field("jung_gu")
    jungrang_gu = make_gu_field("jungrang_gu")
