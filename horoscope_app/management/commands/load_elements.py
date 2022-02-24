import json

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.dateparse import parse_date

from horoscope_app.models import Elements


class Command(BaseCommand):  # https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/
    help = 'Load element to db'

    @transaction.atomic  # инструмент управления транзакциями базы данных
    def handle(self, *args, **options):
        Elements.objects.all().delete()  # очищаем базу данных перед тем как заполнить таблицу

        with open('horoscope_app/fixtures/elements.json') as file:
            elements = json.load(file)  # метод считывает файл в формате JSON и возвращает объекты Python

        to_create = []  # плохая практика обращатьтся к базе в цикле.
        for element in elements:
            to_create.append(Elements(
                name=element['name'],
                code=element['code'],
                ))
        Elements.objects.bulk_create(to_create)  # одним действием отправляем все в базу