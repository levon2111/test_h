# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 15:09
from __future__ import unicode_literals

import apps.users.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_payments'),
        ('users', '0017_companytechnicalstack_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Company')),
            ],
            options={
                'verbose_name_plural': 'Company Portfolio Projects',
            },
        ),
        migrations.CreateModel(
            name='CompanyProjectsImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.users.models.get_file_portfolio_path)),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CompanyProjects')),
            ],
            options={
                'verbose_name_plural': 'Project Images',
            },
        ),
        migrations.CreateModel(
            name='CompanyProjectsTechnologies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CompanyProjects')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Technologies')),
            ],
            options={
                'verbose_name_plural': 'Project Technologies',
            },
        ),
        migrations.CreateModel(
            name='SpecificFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.users.models.get_file_portfolio_path)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CompanyProjects')),
            ],
            options={
                'verbose_name_plural': 'Project Specific features',
            },
        ),
    ]
