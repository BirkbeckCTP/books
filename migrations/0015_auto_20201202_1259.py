# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-02 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20201119_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='chapter_name',
            field=models.CharField(default='chapter', max_length=200),
        ),
        migrations.AddField(
            model_name='category',
            name='chapter_name_plural',
            field=models.CharField(default='chapters', max_length=200),
        ),
    ]
