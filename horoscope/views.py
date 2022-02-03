from django import template
from django.http import response
from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from horoscope.models import ZodiakSing, Elements
from django.template.loader import render_to_string
from .forms import ZodiakSingForm

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

def calendar(request):
    error = ''
    if request.method == 'POST':
        form = ZodiakSingForm(request.POST)
        if form.is_valid():
            # form.save()
            return redirect('index')
        else:
            error = 'Форма была неверной'


    form = ZodiakSingForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'horoscope/calendar.html', context=data)
