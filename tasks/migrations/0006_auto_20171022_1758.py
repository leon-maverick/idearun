# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-22 17:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20171022_1755'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='groups',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='group_title',
            new_name='category_title',
        ),
    ]