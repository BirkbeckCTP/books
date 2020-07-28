# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-28 14:41
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import plugins.books.models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20190731_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='remote_label',
            field=models.CharField(blank=True, help_text='Label for the remote link. If left blank will display as"View on yourremoteurldomain.com"', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='remote_url',
            field=models.URLField(blank=True, help_text='Set this if you want to have your book link out to a remotewebsite rather than local formats.', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/vol/janeway/src/media'), upload_to=plugins.books.models.cover_images_upload_path),
        ),
    ]
