# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-10 10:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20170110_1025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoe',
            old_name='brand',
            new_name='brand_model',
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='name',
        ),
        migrations.AlterField(
            model_name='note',
            name='author',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
