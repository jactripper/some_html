# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 11:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Curriculum_detail',
            new_name='Detail',
        ),
        migrations.RenameModel(
            old_name='Curriculum_index',
            new_name='Index',
        ),
    ]
