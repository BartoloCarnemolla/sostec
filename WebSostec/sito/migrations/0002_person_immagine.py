# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='immagine',
            field=models.CharField(default='no', max_length=200),
        ),
    ]
