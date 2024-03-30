# Generated by Django 5.0.3 on 2024-03-26 04:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
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
                ('image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]