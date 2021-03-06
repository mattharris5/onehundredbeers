# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-07 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0026_beer_untappd_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='contest_player',
            unique_together=set([('contest', 'player')]),
        ),
    ]
