# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-08 10:28
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import plugins.books.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=300)),
                ('subtitle', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField()),
                ('pages', models.PositiveIntegerField()),
                ('is_edited_volume', models.BooleanField(default=False)),
                ('publisher_name', models.CharField(max_length=100)),
                ('publisher_loc', models.CharField(max_length=100)),
                ('cover', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/ajrbyers/Code/revista/src/media'), upload_to=plugins.books.models.cover_images_upload_path)),
                ('doi', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('affiliation', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('sequence', models.PositiveIntegerField(default=10)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=100)),
                ('sequence', models.PositiveIntegerField(default=10)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
    ]
