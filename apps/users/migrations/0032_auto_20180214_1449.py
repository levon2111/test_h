# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-14 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_auto_20180208_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprojectstechnologies',
            name='technology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CompanyTechnicalStack'),
        ),
    ]
