from django.urls import path
from horoscope import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('type', views.type_page),
    path('type/<urls>', views.type_page_sing),
    path('<int:url>', views.info_about_sing_zodiac_by_number),
    path('<str:url>', views.info_about_sing_zodiac, name = 'sign_zodiac'),
]