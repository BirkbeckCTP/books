# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-07-25 17:04
from __future__ import unicode_literals

import core.model_utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0069_delete_blank_keywords'),
        ('books', '0018_auto_20210813_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeywordBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='KeywordChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='PublisherNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='date_embargo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chapter',
            name='date_embargo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chapter',
            name='date_published',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='number',
            field=models.CharField(blank=True, help_text='The chapter number eg. 7 or VII', max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='keywordchapter',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Chapter'),
        ),
        migrations.AddField(
            model_name='keywordchapter',
            name='keyword',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submission.Keyword'),
        ),
        migrations.AddField(
            model_name='keywordbook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
        ),
        migrations.AddField(
            model_name='keywordbook',
            name='keyword',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submission.Keyword'),
        ),
        migrations.AddField(
            model_name='book',
            name='keywords',
            field=core.model_utils.M2MOrderedThroughField(blank=True, null=True, through='books.KeywordBook', to='submission.Keyword'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher_notes',
            field=models.ManyToManyField(blank=True, help_text='Free-text public publisher notes regarding this book', null=True, related_name='book', to='books.PublisherNote'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='keywords',
            field=core.model_utils.M2MOrderedThroughField(blank=True, null=True, through='books.KeywordChapter', to='submission.Keyword'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='publisher_notes',
            field=models.ManyToManyField(blank=True, help_text='Free-text public publisher notes regarding this book', null=True, related_name='chapter', to='books.PublisherNote'),
        ),
        migrations.AlterUniqueTogether(
            name='keywordchapter',
            unique_together=set([('keyword', 'chapter')]),
        ),
        migrations.AlterUniqueTogether(
            name='keywordbook',
            unique_together=set([('keyword', 'book')]),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='pages',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
