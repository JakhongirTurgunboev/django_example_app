# Generated by Django 5.0.3 on 2024-03-19 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='number_of_clicks',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
