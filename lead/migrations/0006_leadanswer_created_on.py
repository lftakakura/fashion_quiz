# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 14:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0005_leadanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadanswer',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]