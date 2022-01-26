from django.db import models


class ZodiakSing(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=45, unique=True)
    description = models.TextField(blank=True)
    date_from = models.DateField()
    date_to = models.DateField()
    element = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.name} - {self.code} - {self.description}'
