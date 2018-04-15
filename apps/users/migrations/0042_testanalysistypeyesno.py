# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-15 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_testanalysisresults'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestAnalysisTypeYesNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rate_start', models.IntegerField()),
                ('rate_end', models.IntegerField()),
                ('analysis', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'TestAnalysisTypeYesNo',
            },
        ),
    ]
