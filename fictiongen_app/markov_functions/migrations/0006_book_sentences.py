# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markov_functions', '0005_book_lines'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='sentences',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
