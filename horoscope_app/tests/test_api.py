from horoscope_app import views
from rest_framework.test import APITestCase

from django.test import TestCase
import pdb


class ForecastsApiTestCase(APITestCase):
    def test_get_forecast_for_api(self):
        response = views.get_forecast_for_api()
        #pdb.set_trace()
        self.assertEqual(len(response), 13) # количество знаков 13 (12 + general)
        all_sing = set(['general', 'Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы'])
        response_all_sing = set([dict['sing'] for dict in response])
        self.assertEqual(all_sing, response_all_sing) # Проверяем наличие всех знаков в ответе


