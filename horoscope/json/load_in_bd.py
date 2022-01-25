import json
from horoscope.models import ZodiakSing


with open('zodiac_sings.json') as file:
    zodiac_sings = json.load(file)
for element_zodiac_sing in zodiac_sings:
    a = ZodiakSing(name=element_zodiac_sing.get['name'], code=element_zodiac_sing.get['name'])
    a.save()
