# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-27 11:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_specificfeatures_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('rate_start', models.CharField(blank=True, max_length=255, null=True)),
                ('rate_end', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_employees_start', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_employees_end', models.CharField(blank=True, max_length=255, null=True)),
                ('technology', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Project Specific features',
            },
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('company',)]),
        ),
        migrations.AddField(
            model_name='searchhistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
