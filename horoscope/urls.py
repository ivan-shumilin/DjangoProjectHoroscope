from django.urls import path
from horoscope import views

urlpatterns = [
    path('', views.index, name='index'),
    path('type', views.type_page),
    path('type/<urls>', views.type_page_sing),
    path('<int:month>', views.get_sing_zodiac_by_date),
    path('<str:code>', views.get_sing_zodiac, name='sign_zodiac'),
]
