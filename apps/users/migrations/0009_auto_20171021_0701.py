# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-10-21 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20170329_0523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='company',
            new_name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='auth_type',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='contact_person_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]