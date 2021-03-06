# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-09 15:47
from __future__ import unicode_literals

import core.file_system
from django.db import migrations, models
import django.db.models.deletion
import plugins.books.models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20190731_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
            ],
            options={
                'ordering': ('slug',),
            },
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.FileField(blank=True, null=True, storage=core.file_system.JanewayFileSystemStorage(), upload_to=plugins.books.models.cover_images_upload_path),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Category'),
        ),
    ]
