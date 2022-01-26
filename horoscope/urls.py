from django.urls import path
from horoscope import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:url>', views.get_sing_zodiac_by_date),
    path('<str:code>', views.get_sing_zodiac, name='sign_zodiac'),
]
