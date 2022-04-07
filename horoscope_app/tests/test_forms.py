from horoscope_app import views
import datetime
from django.urls import reverse

from horoscope_app.forms import ZodiakSingForm
from horoscope_app.models import ZodiakSing

from django.test import TestCase


class TestHoroscope(TestCase):
    fixtures = ['horoscope_app/tests/fixtures/db.json']

def test_calendar_errors(self):
    response = self.client.post('/calendar/', data={'date_from': '2022-15-02'})
    self.assertEqual(200, response.status_code)
    # self.assertEqual('Enter a valid date.', response.context['form'].errors['date_from'][0])
    self.assertEqual('Некорректные данные', response.context['error'])
    # Поиск в html
    self.assertIn('Поиск знака зодиака по дате', response.content.decode('utf-8'))
    self.assertIn('Некорректные данные', response.content.decode('utf-8'))


def test_calendar(self):
    response = self.client.post('/calendar/', data={'date_from': '2022-01-02'})
    self.assertEqual(302, response.status_code)
    self.assertRedirects(response, '/capricorn')