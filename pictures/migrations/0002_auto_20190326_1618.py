# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-26 13:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='like',
            new_name='likes',
        ),
    ]
