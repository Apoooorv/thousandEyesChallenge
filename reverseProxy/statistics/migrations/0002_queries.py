# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endPoint', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
