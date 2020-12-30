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

author = 'Kyubum Moon'

doc = """
행동경제학 관점에서 본 포스트 코로나 시대의 서울시의회의 역할과 과제
"""


class Constants(BaseConstants):
    name_in_url = 'treatment'
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


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    districts = models.IntegerField(
        label = "귀하의 지역구를 선택해주십시오.",
        choices = Constants.DISTRICTS,
        widget = widgets.RadioSelect,
    )
    gangnam_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "논현1동, 신사동, 압구정동, 청담동"],
            [2, "논현2동, 역삼1동, 역삼2동"],
            [3, "개포1동, 개포2동, 개포4동, 일원1동, 일원2동"],
            [4, "세곡동, 수서동, 일월본동"],
            [5, "대치1동, 대치4동, 도곡1동, 도곡2동"],
            [6, "대치2동, 삼성1동, 삼성2동"],
        ],
        widget=widgets.RadioSelect,
    )
    gangdong_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "강일동, 고덕제1동, 고덕제2동, 암사제1동, 암사제2동, 암사제3동"],
            [2, "길동, 명일제1동, 명일제2동, 상일동"],
            [3, "천호제1동, 천호제2동, 천호제3동"],
            [4, "둔촌제2동, 성내제1동, 성내제2동, 성내제3동"],

        ],
        widget=widgets.RadioSelect,
    )
    gangbuk_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "수유제1동, 우이동, 인수동"],
            [2, "삼각산동, 삼양동, 송천동"],
            [3, "미아동, 번제3동, 송중동"],
        ],
        widget=widgets.RadioSelect,
    )
    gangseo_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "화곡제1동, 화곡제2동, 화곡제8동"],
            [2, "발산제1동, 우장산동, 화곡제3동"],
            [3, "공항동, 방화제1동, 방화제2동"],
            [4, "가양제1동, 가양제2동, 등촌제3동, 방화제3동"],
            [5, "가양제3동, 등촌제1동, 염창동"],
            [6, "등촌제2동, 화곡본동, 화곡제4동, 화곡제6동"],
        ],
        widget=widgets.RadioSelect,
    )
    gwanak_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "보라매동, 신림동, 은천동, 중앙동, 청룡동"],
            [2, "낙성대동, 남현동, 성현동, 인헌동, 청림동, 행운동"],
            [3, "난곡동, 난향동, 미성동, 신사동, 조원동"],
            [4, "대학동, 삼성동, 서림동, 서원동, 신원동"],
        ],
        widget=widgets.RadioSelect,
    )
    gwangjin_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "중곡제1동, 중곡제2동, 중곡제3동, 중곡제4동"],
            [2, "광장동, 구의제2동, 군자동, 능동"],
            [3, "구의제1동, 구의제3동, 자양제1동, 자양제2동"],
            [4, "자양제3동, 자양제4동, 화양동"],
        ],
        widget=widgets.RadioSelect,
    )
    guro_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "가리봉동, 구로제3동, 구로제4동"],
            [2, "구로제1동, 구로제2동, 구로제5동, 신도림동"],
            [3, "개봉제1동, 개봉제2동, 개봉제3동, 고척제1동, 고척제2동"],
            [4, "수궁동, 오류제1동, 오류제2동"],
        ],
        widget=widgets.RadioSelect,
    )
    geumcheon_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "가산동, 독산제1동, 독산제2동, 독산제3동, 독산제4동"],
            [2, "시흥제1동, 시흥제2동, 시흥제3동, 시흥제4동, 시흥제5동"],
        ],
        widget=widgets.RadioSelect,
    )
    nowon_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "월계1동, 월계2동, 월계3동"],
            [2, "공릉1동, 공릉2동"],
            [3, "중계1동, 중계4동, 중계본동, 하계1동"],
            [4, "상계6·7동, 중계2·3동, 하계2동"],
            [5, "상계2동, 상계3·4동, 상계5동"],
            [6, "상계10동, 상계1동, 상계8동, 상계9동"],
        ],
        widget=widgets.RadioSelect,
    )
    dobong_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "창1동, 창4동, 창5동"],
            [2, "쌍문1동, 쌍문3동, 창2동, 창3동"],
            [3, "방학3동, 쌍문2동, 쌍문4동"],
            [4, "도봉1동, 도봉2동, 방학1동, 방학2동"],
        ],
        widget=widgets.RadioSelect,
    )
    dongdaemun_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "용신동, 제기동, 청량리동"],
            [2, "이문제1동, 이문제2동, 회기동, 휘경제1동, 휘경제2동"],
            [3, "답십리제1동, 전농제1동, 전농제2동"],
            [4, "답십리제2동, 장안제1동, 장안제2동"],
        ],
        widget=widgets.RadioSelect,
    )
    dongjak_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "노량진제1동, 노량진제2동, 상도제2동, 상도제4동"],
            [2, "대방동, 상도제3동, 신대방제1동, 신대방제2동"],
            [3, "사당제3동, 사당제4동, 사당제5동, 상도제1동"],
            [4, "사당제1동, 사당제2동, 흑석동"],

        ],
        widget=widgets.RadioSelect,
    )
    mapo_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "대흥동, 신수동, 염리동, 용강동"],
            [2, "공덕동, 도화동, 아현동"],
            [3, "망원1동, 서강동, 서교동, 합정동"],
            [4, "망원2동, 상암동, 성산1동, 성산2동, 연남동"],
        ],
        widget=widgets.RadioSelect,
    )
    seodaemun_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "북아현동, 신촌동, 천연동, 충현동"],
            [2, "연희동, 홍제제1동, 홍제제2동"],
            [3, "홍은제1동, 홍은제2동, 홍제제3동"],
            [4, "남가좌제1동, 남가좌제2동, 북가좌제1동, 북가좌제2동"],
        ],
        widget=widgets.RadioSelect,
    )
    seocho_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "반포1동, 반포3동, 반포4동, 잠원동"],
            [2, "반포2동, 반포본동, 방배1동, 방배4동, 방배본동"],
            [3, "내곡동, 서초2동, 서초4동, 양재1동, 양재2동"],
            [4, "방배2동, 방배3동, 서초1동, 서초3동"],
        ],
        widget=widgets.RadioSelect,
    )
    seongdong_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "금호1가동, 금호2·3가동, 금호4가동, 옥수동"],
            [2, "성수1가제1동, 성수1가제2동, 성수2가제1동, 성수2가제3동, 응봉동"],
            [3, "왕십리도선동, 왕십리제2동, 행당제1동, 행당제2동"],
            [4, "마장동, 사근동, 송정동, 용답동"],
        ],
        widget=widgets.RadioSelect,
    )
    seongbuk_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "돈암제2동, 동선동, 보문동, 삼선동, 성북동, 안암동"],
            [2, "길음제1동, 정릉제1동, 정릉제2동, 정릉제3동, 정릉제4동"],
            [3, "길음제2동, 돈암제1동, 월곡제1동, 월곡제2동, 종암동"],
            [4, "석관동, 장위제1동, 장위제2동, 장위제3동"],
        ],
        widget=widgets.RadioSelect,
    )
    songpa_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "잠실4동, 잠실6동, 풍납1동, 풍납2동"],
            [2, "방이1동, 방이2동, 송파1동, 송파2동, 오륜동"],
            [3, "삼전동, 잠실2동, 잠실3동, 잠실7동, 잠실본동"],
            [4, "가락1동, 문정2동, 석촌동"],
            [5, "가락2동, 가락본동, 문정1동, 오금동"],
            [6, "거여1동, 거여2동, 마천1동, 마천2동, 위례동, 장지동"]
        ],
        widget=widgets.RadioSelect,
    )
    yangcheon_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "목2동, 목3동, 목4동, 목5동"],
            [2, "목1동, 신정1동, 신정2동, 신정6동, 신정7동"],
            [3, "신월1동, 신월3동, 신월4동, 신월5동, 신월7동"],
            [4, "신월2동, 신월6동, 신정3동, 신정4동"],

        ],
        widget=widgets.RadioSelect,
    )
    yeongdeungpo_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "도림동, 문래동, 신길제3동, 영등포본동"],
            [2, "당산제1동, 당산제2동, 양평제1동, 양평제2동, 영등포동"],
            [3, "신길제1동, 신길제4동, 신길제5동, 신길제7동, 여의동"],
            [4, "대림제1동, 대림제2동, 대림제3동, 신길제6동"],
        ],
        widget=widgets.RadioSelect,
    )
    yongsan_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "남영동, 용문동, 원효로제1동, 원효로제2동, 이촌제1동, 이촌제2동, 청파동, 한강로동, 효창동"],
            [2, "보광동, 서빙고동, 용산2가동, 이태원제1동, 이태원제2동, 한남동, 후암동"],
        ],
        widget=widgets.RadioSelect,
    )
    eunpyung_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "녹번동, 응암제1동, 응암제2동, 응암제3동"],
            [2, "수색동, 신사제1동, 신사제2동, 역촌동, 증산동"],
            [3, "갈현제1동, 갈현제2동, 진관동"],
            [4, "구산동, 대조동, 불광제1동, 불광제2동"],
        ],
        widget=widgets.RadioSelect,
    )
    jongro_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "가회동, 교남동, 무악동, 부암동, 사직동, 삼청동, 청운효자동, 평창동"],
            [2, "숭인제1동, 숭인제2동, 이화동, 종로1·2·3·4가동, 종로5·6가동, 창신제1동, 창신제2동, 창신제3동, 혜화동"],
        ],
        widget=widgets.RadioSelect,
    )
    jung_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "광희동, 동화동, 명동, 소공동, 신당동, 신당제5동, 을지로동, 중림동, 황학동"],
            [2, "다산동, 약수동, 장충동, 청구동, 필동, 회현동"],

        ],
        widget=widgets.RadioSelect,
    )
    jungrang_gu = models.IntegerField(
        label="귀하의 거주구역을 선택해주십시오.",
        choices=[
            [1, "망우제3동, 면목제3·8동, 면목제4동, 면목제7동"],
            [2, "면목본동, 면목제2동, 면목제5동, 상봉제2동"],
            [3, "묵제1동, 묵제2동, 중화제1동, 중화제2동"],
            [4, "망우본동, 상봉제1동, 신내제1동, 신내제2동"],
        ],
        widget=widgets.RadioSelect,
    )


