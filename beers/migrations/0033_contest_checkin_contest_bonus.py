# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-20 00:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0032_remove_contest_player_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest_checkin',
            name='contest_bonus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beers.Contest_Bonus'),
        ),
    ]
