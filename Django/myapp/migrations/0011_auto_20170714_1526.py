# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-07-14 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20170714_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblog',
            name='weblog_date',
            field=models.DateTimeField(max_length=50),
        ),
    ]
