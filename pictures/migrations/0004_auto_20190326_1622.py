# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-26 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0003_auto_20190326_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='like',
            name='profile',
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['name']},
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
