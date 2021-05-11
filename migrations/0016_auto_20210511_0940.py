# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-11 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_auto_20201202_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_page_title', models.CharField(default='Published Books', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='chapter_name',
            field=models.CharField(default='Chapter', max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='chapter_name_plural',
            field=models.CharField(default='Chapters', max_length=200),
        ),
    ]
