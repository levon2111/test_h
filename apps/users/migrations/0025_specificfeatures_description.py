# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-14 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20171214_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='specificfeatures',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
