from django.db import models


class ZodiacSing(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=45, unique=True)
    description = models.TextField(blank=True)
    date_from = models.DateField()
    date_to = models.DateField()
    element = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.name} - {self.code} - {self.description}'


class ZodiakSingTest(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

#       'name': 'Овен',
#       'code': 'aries',
#       'desc': 'Первый знак зодиака, планета Марс.',
#       'date_from': '21.03.00',
#       'date_to': '20.04.00',
#       'element': 'fire',
