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
            name='Artikel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=30)),
                ('zeit_erstellt', models.DateTimeField(auto_now_add=True)),
                ('inhalt', models.TextField()),
                ('inhalt_nur_fuer_angemeldet', models.TextField(blank=True, null=True)),
                ('datum_publizieren', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-datum_publizieren'],
                'verbose_name_plural': 'Artikel',
            },
        ),
        migrations.CreateModel(
            name='Buechlein',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=30)),
                ('zeit_erstellt', models.DateTimeField(auto_now_add=True)),
                ('pdf', models.FileField(null=True, upload_to='scholienbuechlein')),
                ('bild', models.ImageField(null=True, upload_to='scholienbuechlein')),
                ('beschreibung', models.TextField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Büchlein',
            },
        ),
    ]
