# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-01 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_company_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='foundation_year',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
