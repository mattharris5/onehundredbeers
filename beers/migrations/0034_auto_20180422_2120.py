# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-23 01:20
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0033_contest_checkin_contest_bonus'),
    ]

    operations = [
        migrations.AddField(
            model_name='unvalidated_checkin',
            name='has_possibles',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unvalidated_checkin',
            name='possible_bonuses',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=None, null=True, size=None),
        ),
    ]
