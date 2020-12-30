from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class districtChk(Page):
    form_model = 'player'
    form_fields = [
        'districts',
    ]


class gangnamgu(Page):
    form_model = 'player'
    form_fields = [
        'gangnam_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 1


class gangdonggu(Page):
    form_model = 'player'
    form_fields = [
        'gangdong_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 2


class gangbukgu(Page):
    form_model = 'player'
    form_fields = [
        'gangbuk_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 3


class gangseogu(Page):
    form_model = 'player'
    form_fields = [
        'gangseo_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 4


class gwanakgu(Page):
    form_model = 'player'
    form_fields = [
        'gwanak_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 5


class gwangjingu(Page):
    form_model = 'player'
    form_fields = [
        'gwangjin_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 6


class gurogu(Page):
    form_model = 'player'
    form_fields = [
        'guro_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 7


class geumcheongu(Page):
    form_model = 'player'
    form_fields = [
        'geumcheon_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 8


class nowongu(Page):
    form_model = 'player'
    form_fields = [
        'nowon_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 9


class dobonggu(Page):
    form_model = 'player'
    form_fields = [
        'dobong_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 10


class dongdaemungu(Page):
    form_model = 'player'
    form_fields = [
        'dongdaemun_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 11


class dongjakgu(Page):
    form_model = 'player'
    form_fields = [
        'dongjak_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 12


class mapogu(Page):
    form_model = 'player'
    form_fields = [
        'mapo_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 13


class seodaemungu(Page):
    form_model = 'player'
    form_fields = [
        'seodaemun_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 14


class seochogu(Page):
    form_model = 'player'
    form_fields = [
        'seocho_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 15


class seongdonggu(Page):
    form_model = 'player'
    form_fields = [
        'seongdong_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 16


class seongbukgu(Page):
    form_model = 'player'
    form_fields = [
        'seongbuk_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 17


class songpagu(Page):
    form_model = 'player'
    form_fields = [
        'songpa_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 18


class yangcheongu(Page):
    form_model = 'player'
    form_fields = [
        'yangcheon_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 19


class yeongdeungpogu(Page):
    form_model = 'player'
    form_fields = [
        'yeongdeungpo_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 20


class yongsangu(Page):
    form_model = 'player'
    form_fields = [
        'yongsan_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 21


class eunpyunggu(Page):
    form_model = 'player'
    form_fields = [
        'eunpyung_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 22


class jongrogu(Page):
    form_model = 'player'
    form_fields = [
        'jongro_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 23


class junggu(Page):
    form_model = 'player'
    form_fields = [
        'jung_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 24


class jungranggu(Page):
    form_model = 'player'
    form_fields = [
        'jungrang_gu',
    ]

    def is_displayed(self):
        return self.player.districts == 25


class gangnam_1(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.gangnam_gu == 1


class gangnam_2(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.gangnam_gu == 2


class gangnam_3(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.gangnam_gu == 3


class gangnam_4(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.gangnam_gu == 4


class gangnam_5(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.gangnam_gu == 5


class gangnam_6(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.gangnam_gu == 6


class gangdong_1(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.gangdong_gu == 1


class gangdong_2(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.gangdong_gu == 2


class gangdong_3(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.gangdong_gu == 3


class gangdong_4(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.gangdong_gu == 4


class gangbuk_1(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.gangbuk_gu == 1


class gangbuk_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.gangbuk_gu == 2


class gangbuk_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.gangbuk_gu == 3


class gangseo_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.gangseo_gu == 1


class gangseo_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.gangseo_gu == 2


class gangseo_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.gangseo_gu == 3


class gangseo_4(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.gangseo_gu == 4


class gangseo_5(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.gangseo_gu == 5


class gangseo_6(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.gangseo_gu == 6


class gwanak_1(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.gwanak_gu == 1


class gwanak_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.gwanak_gu == 2


class gwanak_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.gwanak_gu == 3


class gwanak_4(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.gwanak_gu == 4


class guro_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.guro_gu == 1


class guro_2(Page):
    form_model = 'player'
    form_fields = [
    ]

    def is_displayed(self):
        return self.player.guro_gu == 2


class guro_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.guro_gu == 3


class guro_4(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.guro_gu == 4


class geumcheon_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.geumcheon_gu == 1


class geumcheon_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.geumcheon_gu == 2


class nowon_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.nowon_gu == 1


class nowon_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.nowon_gu == 2


class nowon_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.nowon_gu == 3


class nowon_4(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.nowon_gu == 4


class nowon_5(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.nowon_gu == 5


class nowon_6(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.nowon_gu == 6


class dobong_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.dobong_gu == 1


class dobong_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.dobong_gu == 2


class dobong_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.dobong_gu == 3


class dobong_4(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.dobong_gu == 4


class dongdaemun_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.dongdaemun_gu == 1


class dongdaemun_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.dongdaemun_gu == 2


class dongdaemun_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.dongdaemun_gu == 3


class dongdaemun_4(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.dongdaemun_gu == 4


class dongjak_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.dongjak_gu == 1


class dongjak_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.dongjak_gu == 2


class dongjak_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.dongjak_gu == 3


class dongjak_4(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.dongjak_gu == 4


class mapo_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.mapo_gu == 1


class mapo_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.mapo_gu == 2


class mapo_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.mapo_gu == 3


class mapo_4(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.mapo_gu == 4


class seocho_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.seocho_gu == 1


class seocho_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.seocho_gu == 2


class seocho_3(Page):
    form_model = 'player'
    form_fields = [
    ]

    def is_displayed(self):
        return self.player.seocho_gu == 3


class seocho_4(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.seocho_gu == 4


class seongdong_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.seongdong_gu == 1


class seongdong_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.seongdong_gu == 2


class seongdong_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.seongdong_gu == 3


class seongdong_4(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.seongdong_gu == 4


class seongbuk_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.seongbuk_gu == 1


class seongbuk_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.seongbuk_gu == 2


class seongbuk_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.seongbuk_gu == 3


class seongbuk_4(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.seongbuk_gu == 4


class songpa_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.songpa_gu == 1


class songpa_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.songpa_gu == 2


class songpa_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.songpa_gu == 3


class songpa_4(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.songpa_gu == 4


class songpa_5(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.songpa_gu == 5


class songpa_6(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.songpa_gu == 6


class yangcheon_1(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.yangcheon_gu == 1


class yangcheon_2(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.yangcheon_gu == 2


class yangcheon_3(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.yangcheon_gu == 3


class yangcheon_4(Page):
    form_model = 'player'
    form_fields = [

    ]

    def is_displayed(self):
        return self.player.yangcheon_gu == 4


class yeongdeungpo_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.yeongdeungpo_gu == 1


class yeongdeungpo_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.yeongdeungpo_gu == 2


class yeongdeungpo_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.yeongdeungpo_gu == 3


class yeongdeungpo_4(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.yeongdeungpo_gu == 4


class yongsan_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.yongsan_gu == 1


class yongsan_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.yongsan_gu == 2


class eunpyung_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.eunpyung_gu == 1


class eunpyung_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.eunpyung_gu == 2


class eunpyung_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.eunpyung_gu == 3


class eunpyung_4(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.eunpyung_gu == 4


class jongro_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.jongro_gu == 1


class jongro_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.jongro_gu == 2


class jung_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.jung_gu == 1


class jung_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.jung_gu == 2


class jungrang_1(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.jungrang_gu == 1


class jungrang_2(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.jungrang_gu == 2


class jungrang_3(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.jungrang_gu == 3


class jungrang_4(Page):
    form_model = 'player'
    form_fields = []

    def is_displayed(self):
        return self.player.jungrang_gu == 4

class gwangjin_1(Page):
    form_model='player'
    form_fields = []
    def is_displayed(self):
        return self.player.gwangjin_gu==1

class gwangjin_2(Page):
    form_model='player'
    form_fields = []
    def is_displayed(self):
        return self.player.gwangjin_gu==2
class gwangjin_3(Page):
    form_model='player'
    form_fields = []
    def is_displayed(self):
        return self.player.gwangjin_gu==3
class gwangjin_4(Page):
    form_model='player'
    form_fields = []
    def is_displayed(self):
        return self.player.gwangjin_gu==4
class seodaemun_1(Page):
    form_model='player'
    form_fields = []
    def is_displayed(self):
        return self.player.seodaemun_gu==1

class seodaemun_2(Page):
    form_model='player'
    form_fields = []
    def is_displayed(self):
        return self.player.seodaemun_gu==2
class seodaemun_3(Page):
    form_model='player'
    form_fields = []
    def is_displayed(self):
        return self.player.seodaemun_gu==3
class seodaemun_4(Page):
    form_model='player'
    form_fields = []
    def is_displayed(self):
        return self.player.seodaemun_gu==4


page_sequence = [districtChk, gangnamgu, gangdonggu, gangbukgu, gangseogu, gwanakgu, gwangjingu, gurogu, geumcheongu,
                 dobonggu, dongdaemungu, dongjakgu, mapogu, seodaemungu, seochogu, seongdonggu, seongbukgu, songpagu,
                 yangcheongu,
                 yeongdeungpogu, yongsangu, eunpyunggu, jongrogu, junggu, jungranggu, nowongu, gangnam_1, gangnam_2,
                 gangnam_3,
                 gangnam_4, gangnam_5, gangnam_6, gangdong_1, gangdong_2, gangdong_3, gangdong_4,
                 gangbuk_1, gangbuk_2, gangbuk_3, gangseo_1, gangseo_2, gangseo_3, gangseo_4, gangseo_5, gangseo_6,
                 gwanak_1, gwanak_2, gwanak_3, gwanak_4,
                 guro_1, guro_2, guro_3, guro_4, geumcheon_1, geumcheon_2, nowon_1, nowon_2, nowon_3, nowon_4, nowon_5,
                 nowon_6, dobong_1, dobong_2, dobong_3, dobong_4, dongdaemun_1, dongdaemun_2, dongdaemun_3,
                 dongdaemun_4,
                 dongjak_1, dongjak_2, dongjak_3, dongjak_4, mapo_1, mapo_2, mapo_3, mapo_4,
                 seocho_1, seocho_2, seocho_3, seocho_4, seongdong_1, seongdong_2, seongdong_3, seongdong_4,
                 seongbuk_1, seongbuk_2, seongbuk_3, seongbuk_4, songpa_1, songpa_2, songpa_3, songpa_4, songpa_5,
                 songpa_6,
                 yangcheon_1, yangcheon_2, yangcheon_3, yangcheon_4, yeongdeungpo_1, yeongdeungpo_2, yeongdeungpo_3,
                 yeongdeungpo_4,
                 yongsan_1, yongsan_2, eunpyung_1, eunpyung_2, eunpyung_3, eunpyung_4, jongro_1, jongro_2, jung_1,
                 jung_2,
                 jungrang_1, jungrang_2, jungrang_3, jungrang_4,gwangjin_1,gwangjin_2,gwangjin_3,gwangjin_4,
                 seodaemun_1, seodaemun_2, seodaemun_3, seodaemun_4,
                 ]
