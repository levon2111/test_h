# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-10 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170307_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_confirmation_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='reset_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]