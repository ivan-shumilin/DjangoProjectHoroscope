from django import template
from django.http import response
from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from horoscope.models import ZodiakSing, Elements
from django.template.loader import render_to_string
from .forms import ZodiakSingForm
from django.db.models import Q


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


def get_elements(request):
    context = {
        'elements': Elements.objects.all(),
    }
    return render(request, 'horoscope/get_elements.html', context=context)


def get_sing_zodiac_by_date(request, date):
    pass


def get_sing_by_element_name(request, code):
    context = {
        'zodiac_sings': ZodiakSing.objects.all(),
        'element': Elements.objects.get(code=code),
        'elements': ZodiakSing.objects.filter(elements_id=(Elements.objects.get(code=code).id)),
    }
    return render(request, 'horoscope/get_sing_by_element_name.html', context=context)

def search_sing_by_date(date):
    if date.month == 1 and date.day < 21:
        return (ZodiakSing.objects.get(code='capricorn')).code

    if ZodiakSing.objects.filter(Q(date_from__day__lte=date.day) & Q(date_from__month=date.month)):
        return (ZodiakSing.objects.get(Q(date_from__day__lte=date.day) & Q(date_from__month=date.month))).code
    else:
        return (ZodiakSing.objects.get(Q(date_from__month=(date.month - 1)))).code


def calendar(request):
    error = ''
    if request.method == 'POST':
        form = ZodiakSingForm(request.POST)
        if form.is_valid():
            # form.save()
            # return HttpResponse(form.cleaned_data["date_from"].day)
            # return render(request, 'horoscope/calendar.html', context={'date_input': form.cleaned_data["date_from"]})
            # return redirect(search_sing_by_date(form.cleaned_data["date_from"]))
            return redirect(f'/{search_sing_by_date(form.cleaned_data["date_from"])}')
        else:
            error = 'Некорректные данные'
    form = ZodiakSingForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'horoscope/calendar.html', context=data)