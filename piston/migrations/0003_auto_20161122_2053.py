# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piston', '0002_auto_20161106_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='timestamp',
            field=models.IntegerField(default=1),
        ),
    ]
