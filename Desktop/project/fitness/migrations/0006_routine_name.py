# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-26 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0005_routine_exercises'),
    ]

    operations = [
        migrations.AddField(
            model_name='routine',
            name='name',
            field=models.TextField(auto_created=True, null=True),
        ),
    ]
