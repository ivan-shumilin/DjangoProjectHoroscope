from django.db import models
from datetime import date

# Create your models here.
class Forecast(models.Model):
    sing = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=5000, null=True)
    date_create = models.DateField(default=date.today)

    def __str__(self):
        return f'{self.sing} - {self.description}'


class Elements(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return f'{self.name}'


class ZodiakSing(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=45, unique=True)
    description = models.TextField(blank=True)
    date_from = models.DateField()
    date_to = models.DateField()
    elements = models.ForeignKey(Elements, on_delete=models.PROTECT)

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name} - {self.code} - {self.description}'
