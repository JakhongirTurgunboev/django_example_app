# Generated by Django 5.0.3 on 2024-03-16 04:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vacancy', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('experience', models.FloatField(default=0)),
                ('location', models.CharField(max_length=250)),
                ('min_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comf_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('birth_date', models.DateField()),
                ('tags', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.vacancy')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.profile')),
            ],
        ),
    ]
