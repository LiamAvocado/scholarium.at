# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-05-11 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veranstaltungen', '0007_auto_20170511_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studiumdings',
            options={'ordering': ['reihenfolge'], 'verbose_name_plural': 'Studiendinger'},
        ),
        migrations.AddField(
            model_name='studiumdings',
            name='reihenfolge',
            field=models.SmallIntegerField(null=True),
        ),
    ]