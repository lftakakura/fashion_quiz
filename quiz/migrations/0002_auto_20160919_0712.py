# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_title',
            field=models.TextField(verbose_name='pergunta'),
        ),
    ]