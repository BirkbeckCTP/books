# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-08 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_published',
            field=models.DateField(blank=True, null=True),
        ),
    ]