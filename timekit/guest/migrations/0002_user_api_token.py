# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='api_token',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
