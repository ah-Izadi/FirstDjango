# Generated by Django 4.2.3 on 2023-08-01 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Date_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
