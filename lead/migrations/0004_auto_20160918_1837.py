# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0003_auto_20160918_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='idade'),
        ),
        migrations.AddField(
            model_name='lead',
            name='gender',
            field=models.PositiveIntegerField(choices=[(0, 'Masculino'), (1, 'Feminino')], null=True, verbose_name='sexo'),
        ),
    ]
