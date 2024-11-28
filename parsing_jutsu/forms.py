from django import forms
from . import models, parsing_jutsu


class ParserForm(forms.Form):
    MEDIA_CHOICES = (("jutsu", "jutsu"),)
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            "media_type",
        ]

    def parser_data(self):
        if self.data["media_type"] == "jutsu":
            jutsu_pars = parsing_jutsu.parsing()
            for i in jutsu_pars:
                models.Jutsu.objects.create(**i)