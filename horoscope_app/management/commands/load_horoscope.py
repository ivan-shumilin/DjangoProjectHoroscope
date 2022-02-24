import json

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.dateparse import parse_date

from horoscope_app.models import ZodiakSing, Elements


class Command(BaseCommand):  # https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/
    help = 'Load horoscope_app sings to db'

    @transaction.atomic  # инструмент управления транзакциями базы данных
    def handle(self, *args, **options):
        ZodiakSing.objects.all().delete()  # очищаем базу данных перед тем как заполнить таблицу

        with open('horoscope_app/fixtures/zodiac_sings.json') as file:
            zodiac_sings = json.load(file)  # метод считывает файл в формате JSON и возвращает объекты Python

        to_create = []  # плохая практика обращатьтся к базе в цикле.
        for zodiac_sing in zodiac_sings:
            to_create.append(ZodiakSing(
                name=zodiac_sing['name'],
                code=zodiac_sing['code'],
                description=zodiac_sing['desc'],
                date_from=parse_date(zodiac_sing['date_from']),
                date_to=parse_date(zodiac_sing['date_to']),
                elements=Elements.objects.get(code=zodiac_sing['element']),
            ))
        ZodiakSing.objects.bulk_create(to_create)  # одним действием отправляем все в базу