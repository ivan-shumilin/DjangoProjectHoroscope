# Generated by Django 4.0 on 2022-01-25 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZodiakSingTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]