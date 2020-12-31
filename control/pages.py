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

class control_pg(Page):
    form_model = 'player'
    form_fields = []

page_sequence = [districtChk, gangnamgu, gangdonggu, gangbukgu, gangseogu, gwanakgu, gwangjingu, gurogu, geumcheongu,
                 dobonggu, dongdaemungu, dongjakgu, mapogu, seodaemungu, seochogu, seongdonggu, seongbukgu, songpagu,
                 yangcheongu,
                 yeongdeungpogu, yongsangu, eunpyunggu, jongrogu, junggu, jungranggu, nowongu,control_pg,
                 ]
