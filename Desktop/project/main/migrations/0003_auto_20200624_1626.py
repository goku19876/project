# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-24 16:26
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200623_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='equipment_needed',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('BARBELL', 'Barbell'), ('DUMBBELL', 'Dumbbell'), ('KETTLEBELL', 'Kettlebell'), ('PULLUPBAR', 'Pullup Bar'), ('FOAMROLLER', 'Foam roller'), ('PLATES', 'Plates')], max_length=55),
        ),
    ]
