# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_auto_20170409_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='ask_time',
            field=models.DateTimeField(default='2017-4-17T09:21:31+0000'),
        ),
    ]
