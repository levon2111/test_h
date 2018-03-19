# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 07:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20171031_0633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('confirmed_by_client', models.BooleanField(default=False)),
                ('confirmed_by_company', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Company')),
            ],
            options={
                'verbose_name_plural': 'Cooperation',
            },
        ),
    ]