# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-23 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_companyprojects_companyprojectsimages_companyprojectstechnologies_specificfeatures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companytechnicalstack',
            name='rate',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
    ]
