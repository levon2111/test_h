# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-27 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_auto_20180327_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='testquestionanswers',
            name='correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='testquestionanswers',
            name='rate',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
