from django.shortcuts import render, redirect
from horoscope_app.models import ZodiakSing, Elements, Forecast
from .forms import ZodiakSingForm
from django.db.models import Q
from django.views import generic
import requests, datetime

from django.core.management.base import BaseCommand
from django.db import transaction


#
# Как оптимизировать?
#


@transaction.atomic  # инструмент управления транзакциями базы данных
def load_forecast():
    """Записывает прогноз в формате json в модель Forecast"""
    # если в Forecast нет прогноза за сегодня делаем запрос на получение
    if datetime.date.today() != Forecast.objects.get(sing='general').date_create:
        Forecast.objects.all().delete()  # очищаем базу данных перед тем как заполнить таблицу
        forecasts = get_forecast_for_api()
        to_create = []
        for forecast in forecasts:
            to_create.append(Forecast(
                sing=forecast['sing'],
                description=forecast['description'],
            ))
        Forecast.objects.bulk_create(to_create)


def get_forecast_for_api():
    """ Получаем прогноз по api """
    url = 'https://intense-badlands-65950.herokuapp.com/api/forecast/'  # Полный адрес эндпоинта
    headers = {'authorization': 'Token 16058768c24b66535820533ba5fabd3381cc8905',
               'content-type': 'application/json', }
    response = requests.get(url, headers=headers)  # Делаем GET-запрос
    # Поскольку данные пришли в формате json, переведем их в python
    response_on_python = response.json()
    return response_on_python


class IndexListView(generic.ListView):
    model = ZodiakSing
    # Определение имени шаблона и его расположения
    template_name = 'horoscope_app/index.html'

    def get_context_data(self, **kwargs):
        load_forecast()  # куда добавлять функцию для исполнения?
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['forecast_general'] = Forecast.objects.get(sing='general')  # общий прогнроз для всх знаков
        context['forecast'] = Forecast.objects.all()
        context['today'] = datetime.date.today()
        return context


def get_sing_zodiac(request, code):
    """Вывод информации о каждом знаке"""
    zodiac_sing = ZodiakSing.objects.get(code=code)
    context = {
        'zodiac_sing': zodiac_sing,
        'forecast_zodiac_sing': Forecast.objects.get(sing=zodiac_sing.name),
        'zodiac_sings': ZodiakSing.objects.all(),
    }
    return render(request, 'horoscope_app/info_zodiac.html', context=context)


class ElementsView(generic.ListView):
    """Вывод 4х стихий"""
    model = Elements
    template_name = 'horoscope_app/get_elements.html'


def get_sing_by_element_name(request, code):
    context = {
        'zodiac_sings': ZodiakSing.objects.all(),
        'element': Elements.objects.get(code=code),
        'elements': ZodiakSing.objects.filter(elements_id=(Elements.objects.get(code=code).id)),
    }
    return render(request, 'horoscope_app/get_sing_by_element_name.html', context=context)


def search_sing_by_date(date):
    sign = ZodiakSing.objects.filter(
        Q(date_from__day__lte=date.day, date_from__month=date.month) |
        Q(date_to__day__gte=date.day, date_to__month=date.month)
    ).order_by('date_to').first()
    return sign.code


def get_sing_zodiac_by_date(request):
    error = ''
    if request.method == 'POST':
        form = ZodiakSingForm(request.POST)
        if form.is_valid():
            return redirect(f'/{search_sing_by_date(form.cleaned_data["date_from"])}')
        else:
            error = 'Некорректные данные'
    form = ZodiakSingForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'horoscope_app/calendar.html', context=data)
