# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_log_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='time',
            field=models.DateTimeField(blank=True, verbose_name='time swiped'),
        ),
    ]
