from django.db import models


# Create your models here.

class Zodiak_sing(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    element = models.ForeignKey('element', on_delete=models.PROTECT, null=True)
    calendar = models.OneToOneField('calendar', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.name} - {self.description}'


class element(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=45)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.description}'


class calendar(models.Model):
    month_from = models.SmallIntegerField(null=True)
    month_to = models.SmallIntegerField(null=True)
    day_from = models.SmallIntegerField(null=True)
    day_to = models.SmallIntegerField(null=True)

    def __str__(self):
        return f'{self.month_from} - {self.month_to} - {self.day_from} - {self.day_to}'
