# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 14:20
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import plugins.books.models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_date_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contributor',
            options={'ordering': ('sequence',)},
        ),
        migrations.AlterModelOptions(
            name='format',
            options={'ordering': ('sequence',)},
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/ajrbyers/Code/janeway/src/media'), upload_to=plugins.books.models.cover_images_upload_path),
        ),
        migrations.AlterField(
            model_name='book',
            name='doi',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='prefix',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
