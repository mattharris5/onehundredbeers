# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-17 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0017_contest_checkin_checkin_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('untappd_id', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=250)),
                ('last_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Contest_Brewery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brewery_name', models.CharField(max_length=250)),
                ('point_value', models.IntegerField(default=1)),
                ('total_visited', models.IntegerField(verbose_name='number of players who drank at this brewery')),
                ('brewery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beers.Brewery')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beers.Contest')),
            ],
        ),
        migrations.AddField(
            model_name='contest_player',
            name='brewery_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contest_player',
            name='last_checkin_brewery',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Denormalized brewery name from last checkin'),
        ),
        migrations.AddField(
            model_name='contest_player',
            name='total_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contest_checkin',
            name='contest_beer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beers.Contest_Beer'),
        ),
        migrations.AddField(
            model_name='contest_checkin',
            name='contest_brewery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beers.Contest_Brewery'),
        ),
    ]
