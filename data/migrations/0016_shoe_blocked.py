# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-19 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_remove_shoe_size_in_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='blocked',
            field=models.BooleanField(default=False),
        ),
    ]