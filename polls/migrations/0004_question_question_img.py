# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 06:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160322_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_img',
            field=models.ImageField(default=datetime.datetime(2016, 3, 23, 6, 54, 56, 552969, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
    ]