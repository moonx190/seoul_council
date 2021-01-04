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


class _treatment(Page):
    form_mode = 'player'
    form_fields = []

    def vars_for_template(self):
        varname_to_eval = "self.player." + Constants.INDEX_GU[self.player.districts]
        print("varname_to_eval=" + varname_to_eval)
        print("and its value=" + str(eval(varname_to_eval)))

        gu_index = self.player.districts
        dong_index = eval(varname_to_eval)
        key_for_council = Constants.INDEX_GU[gu_index] + "_" + str(dong_index)
        url_number = Constants.KEY_COUNCIL_NUMER[key_for_council]
        print("key_for_council:"+key_for_council+", and url_number:"+str(url_number))
        return dict(
            url_number=url_number,
        )


page_sequence = [
    districtChk, _dong_question, _treatment
]
