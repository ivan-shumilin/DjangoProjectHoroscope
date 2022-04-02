from django.shortcuts import render, redirect
from horoscope_app.models import ZodiakSing, Elements
from .forms import ZodiakSingForm
from django.db.models import Q
from django.views import generic
import requests, datetime



# def index(request):
#     context = {
#         'zodiac_sings': ZodiakSing.objects.all(),
#     }
#     return render(request, 'horoscope_app/index.html', context=context)
def get_forecast_for_api():
    url = 'https://intense-badlands-65950.herokuapp.com/api/forecast/'  # Полный адрес эндпоинта
    headers = {'authorization': 'Token 16058768c24b66535820533ba5fabd3381cc8905',
               'content-type': 'application/json', }
    # auth = auth=('user', 'pass')
    response = requests.get(url, headers=headers)  # Делаем GET-запрос
    # Поскольку данные пришли в формате json, переведем их в python
    response_on_python = response.json()
    return response_on_python[0]['description']


class IndexListView(generic.ListView):
    model = ZodiakSing

    # Определение имени шаблона и его расположения
    template_name = 'horoscope_app/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['forecast'] = get_forecast_for_api()
        context['today'] = datetime.date.today()
        return context


def get_sing_zodiac(request, code):
    context = {
        'zodiac_sing': ZodiakSing.objects.get(code=code),
        'zodiac_sings': ZodiakSing.objects.all(),
    }
    return render(request, 'horoscope_app/info_zodiac.html', context=context)


# def get_elements(request):
#     context = {
#         'elements': Elements.objects.all(),
#     }
#     return render(request, 'horoscope_app/get_elements.html', context=context)
class ElementsView(generic.ListView):
    model = Elements
    # Определение имени вашего шаблона и его расположения
    template_name = 'horoscope_app/get_elements.html'


def get_sing_by_element_name(request, code):
    url = 'https://intense-badlands-65950.herokuapp.com/api/forecast/'  # Полный адрес эндпоинта
    response = requests.get(url)  # Делаем GET-запрос
    # Поскольку данные пришли в формате json, переведем их в python
    response_on_python = response.json()
    context = {
        'zodiac_sings': ZodiakSing.objects.all(),
        'element': Elements.objects.get(code=code),
        'elements': ZodiakSing.objects.filter(elements_id=(Elements.objects.get(code=code).id)),
        'forecast': response_on_python,
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
