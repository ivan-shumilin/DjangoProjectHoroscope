import json

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.dateparse import parse_date

from horoscope.models import ZodiacSing


class Command(BaseCommand):
    help = 'Load horoscope sings to db'

    @transaction.atomic
    def handle(self, *args, **options):
        ZodiacSing.objects.all().delete()

        with open('horoscope/fixtures/zodiac_sings.json') as file:
            zodiac_sings = json.load(file)

        to_create = []
        for zodiac_sing in zodiac_sings:
            to_create.append(ZodiacSing(
                name=zodiac_sing['name'],
                code=zodiac_sing['code'],
                description=zodiac_sing['desc'],
                date_from=parse_date(zodiac_sing['date_from']),
                date_to=parse_date(zodiac_sing['date_to']),
                element=zodiac_sing['element'],
            ))
        ZodiacSing.objects.bulk_create(to_create)
