# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-24 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20171022_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('DONE', 'Done')], max_length=1),
        ),
    ]