# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20160717_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
