# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-17 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='locate',
            name='google_map_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
