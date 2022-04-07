from horoscope_app import views

from django.test import TestCase


class ForecastsApiTestCase(APITestCase):
    def test_get_forecast_for_api(self):
        response = views.get_forecast_for_api()
        self.assertEqual(len(response), 13)

