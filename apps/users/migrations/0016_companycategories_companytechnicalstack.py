# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_payments'),
        ('users', '0015_auto_20171031_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ProgramingSections')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Company')),
            ],
            options={
                'verbose_name_plural': 'Company Programming Sections',
            },
        ),
        migrations.CreateModel(
            name='CompanyTechnicalStack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('manual_test_passed', models.BooleanField(default=False)),
                ('automatic_test', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Company')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Technologies')),
            ],
            options={
                'verbose_name_plural': 'Company Technical Stack',
            },
        ),
    ]
