# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-26 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real', models.CharField(max_length=100)),
                ('feel', models.CharField(max_length=100)),
            ],
        ),
    ]
