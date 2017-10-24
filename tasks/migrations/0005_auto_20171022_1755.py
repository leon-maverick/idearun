# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-22 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_title', models.CharField(max_length=80)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='groups',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.groups'),
        ),
    ]