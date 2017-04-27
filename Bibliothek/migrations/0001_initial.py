# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-04-26 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=30)),
                ('zeit_erstellt', models.DateTimeField(auto_now_add=True)),
                ('titel', models.CharField(blank=True, max_length=40, null=True)),
                ('autor', models.CharField(blank=True, max_length=40, null=True)),
                ('isbn', models.CharField(blank=True, max_length=40, null=True)),
                ('adresse', models.CharField(blank=True, max_length=40, null=True)),
                ('ausgabe', models.CharField(blank=True, max_length=40, null=True)),
                ('herausgeber', models.CharField(blank=True, max_length=40, null=True)),
                ('serie', models.CharField(blank=True, max_length=40, null=True)),
                ('notiz', models.CharField(blank=True, max_length=40, null=True)),
                ('jahr', models.CharField(blank=True, max_length=4, null=True)),
                ('sprache', models.CharField(blank=True, max_length=3, null=True)),
                ('exlibris', models.CharField(blank=True, max_length=40, null=True)),
                ('stichworte', models.CharField(blank=True, max_length=200, null=True)),
                ('zusammenfassung', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Bücher',
            },
        ),
    ]
