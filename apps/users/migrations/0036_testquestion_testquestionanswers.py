# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-27 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_learner_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Test')),
            ],
            options={
                'verbose_name_plural': 'TestQuestion',
            },
        ),
        migrations.CreateModel(
            name='TestQuestionAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.TestQuestion')),
            ],
            options={
                'verbose_name_plural': 'TestQuestionAnswer',
            },
        ),
    ]