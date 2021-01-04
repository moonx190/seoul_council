from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class districtChk(Page):
    form_model = 'player'
    form_fields = [
        'districts',
    ]

class _dong_question(Page):
    form_model = 'player'

    def get_form_fields(self):
        return [Constants.INDEX_GU[self.player.districts]]

    def vars_for_template(self):
        print("_dong_question -> vars_to_return")
        print("gu_kor_name="+Constants.INDEX_GU_KOR[self.player.districts])

        vars_to_return = dict(
            gu_kor_name=Constants.INDEX_GU_KOR[self.player.districts]
        )

        return vars_to_return

class control_pg(Page):
    form_model = 'player'
    form_fields = []

page_sequence = [
    districtChk,
    _dong_question,
    control_pg,
]
