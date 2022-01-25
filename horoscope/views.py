from django.shortcuts import render
from horoscope.models import ZodiacSing


def index(request):
    context = {
        'zodiac_sings': ZodiacSing.objects.all(),
    }
    return render(request, 'horoscope/index.html', context=context)


def get_sing_zodiac(request, code):
    context = {
        'zodiac_sing': ZodiacSing.objects.get(code=code),
        'zodiac_sings': ZodiacSing.objects.all(),
    }
    return render(request, 'horoscope/info_zodiac.html', context=context)


def get_sing_zodiac_by_date(request, date):
    pass


def get_sing_by_element_name(request, element):
    pass
