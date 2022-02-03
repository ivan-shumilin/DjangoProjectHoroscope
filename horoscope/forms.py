from horoscope.models import ZodiakSing, Elements
from django.forms import ModelForm, DateInput

class ZodiakSingForm(ModelForm):
    class Meta:
        model = ZodiakSing
        fields = ['date_from']

        widgets = {
            "date_from": DateInput(attrs={
                'type': 'date',
                'class': 'form-conrol',
            })
        }