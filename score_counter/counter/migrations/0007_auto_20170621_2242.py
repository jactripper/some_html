# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0006_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='type_c',
            field=models.TextField(),
        ),
    ]
