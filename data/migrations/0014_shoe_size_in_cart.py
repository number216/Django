# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-14 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_auto_20170112_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='size_in_cart',
            field=models.CharField(default=b'0', max_length=10),
        ),
    ]