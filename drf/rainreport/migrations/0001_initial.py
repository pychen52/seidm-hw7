# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rainfall',
            fields=[
                ('rpk', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('sid', models.CharField(max_length=5)),
                ('timestamp', models.CharField(max_length=25)),
                ('r_10m', models.FloatField(blank=True, null=True)),
                ('r_1h', models.FloatField(blank=True, null=True)),
                ('r_3h', models.FloatField(blank=True, null=True)),
                ('r_6h', models.FloatField(blank=True, null=True)),
                ('r_12h', models.FloatField(blank=True, null=True)),
                ('r_24h', models.FloatField(blank=True, null=True)),
                ('r_td', models.FloatField(blank=True, null=True)),
                ('r_yd', models.FloatField(blank=True, null=True)),
                ('r_2d', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rainfall',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('spk', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('sid', models.CharField(max_length=5)),
                ('county', models.CharField(max_length=3)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
            ],
            options={
                'db_table': 'station',
            },
        ),
    ]
