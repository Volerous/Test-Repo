# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='pubDate',
            new_name='pub_date',
        ),
    ]
