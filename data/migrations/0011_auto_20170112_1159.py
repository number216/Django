# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-12 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_shoe_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
