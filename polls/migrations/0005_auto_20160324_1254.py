# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 06:54
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_question_question_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_img',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b''),
        ),
    ]
