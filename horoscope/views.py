from django import template
from django.http import response
from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from horoscope.models import ZodiakSing
from django.template.loader import render_to_string

# Create your views here.
zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

types_sign_zodiac = {
    'wather': ['cancer', 'scorpio', 'pisces'],
    'fire': ['aries', 'leo', 'sagittarius'],
    'air': ['gemini', 'libra', 'aquarius'],
    'eath': ['taurus', 'capricorn', 'virgo'],
}


def index(request):
    context = {
        'zodiac_sings': ZodiakSing.objects.all(),
    }
    return render(request, 'horoscope/index.html', context=context)


def get_sing_zodiac(request, code):
    context = {
        'zodiac_sing': ZodiakSing.objects.get(code=code),
        'zodiac_sings': ZodiakSing.objects.all(),
    }
    return render(request, 'horoscope/info_zodiac.html', context=context)


def get_sing_zodiac_by_date(request, url: int):
    if url > len(zodiac_dict):
        return HttpResponseNotFound(f'{url} - very big')
    return HttpResponse(zodiac_dict[list(zodiac_dict)[url - 1]])

def get_sing_zodiac_by_date(request, date):
    pass


def get_sing_by_element_name(request, element):
    pass