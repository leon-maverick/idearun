# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-24 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20171024_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
