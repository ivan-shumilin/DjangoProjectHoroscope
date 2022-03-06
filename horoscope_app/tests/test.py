from horoscope_app import views
import datetime

from horoscope_app.forms import ZodiakSingForm
from horoscope_app.models import ZodiakSing

from django.test import TestCase


class TestHoroscope(TestCase):
    fixtures = ['horoscope_app/tests/fixtures/horoscope.json']

    def assert_search_sing_by_date(self, date, sign):
        self.assertEqual(views.search_sing_by_date(date), sign)

    def test_search_sing_by_date(self):
        self.assert_search_sing_by_date(datetime.date(2012, 5, 24), 'gemini')
        self.assert_search_sing_by_date(datetime.date(2012, 6, 27), 'cancer')
        self.assert_search_sing_by_date(datetime.date(2012, 1, 1), 'capricorn')
        self.assert_search_sing_by_date(datetime.date(2012, 10, 14), 'libra')
        self.assert_search_sing_by_date(datetime.date(2012, 11, 14), 'scorpio')
        self.assert_search_sing_by_date(datetime.date(2012, 3, 1), 'pisces')


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

    def test_get_zodiac_sign(self):
        response = self.client.get('/capricorn', data={'date_from': '2022-01-02'})
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.context['zodiac_sing'].id, ZodiakSing.objects.get(code='capricorn').id)
        self.assertEqual(len(response.context['zodiac_sings']), 12)