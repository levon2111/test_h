# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_companycategories_companytechnicalstack'),
    ]

    operations = [
        migrations.AddField(
            model_name='companytechnicalstack',
            name='rate',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
