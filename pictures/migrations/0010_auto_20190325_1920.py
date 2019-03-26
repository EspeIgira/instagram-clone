# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0009_auto_20190325_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]