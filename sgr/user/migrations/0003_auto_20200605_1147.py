# Generated by Django 3.0.6 on 2020-06-05 11:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200602_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='reg_datetime',
            field=models.DateField(default=datetime.datetime(2020, 6, 5, 11, 47, 52, 639942, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='student',
            name='reg_datetime',
            field=models.DateField(default=datetime.datetime(2020, 6, 5, 11, 47, 52, 634982, tzinfo=utc)),
        ),
    ]