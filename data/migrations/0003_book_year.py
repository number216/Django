# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20161117_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(default=0, max_length=4),
        ),
    ]
