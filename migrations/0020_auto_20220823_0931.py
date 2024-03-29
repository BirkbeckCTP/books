# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-08-23 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_auto_20220725_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='custom_how_to_cite',
            field=models.TextField(blank=True, help_text="Custom 'how to cite' text. To be used only if the block generated by Janeway is not suitable.", null=True),
        ),
        migrations.AddField(
            model_name='chapter',
            name='custom_how_to_cite',
            field=models.TextField(blank=True, help_text="Custom 'how to cite' text. To be used only if the block generated by Janeway is not suitable.", null=True),
        ),
    ]
