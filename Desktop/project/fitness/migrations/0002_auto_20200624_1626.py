# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-24 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='id',
        ),
        migrations.AddField(
            model_name='goal',
            name='goal_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
