# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 19:17
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0036_auto_20180506_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest_bonus',
            name='hashtags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=None, max_length=30), default=None, null=True, size=None),
        ),
    ]
