# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 03:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20161009_1806'),
        ('songs', '0004_song_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.User'),
            preserve_default=False,
        ),
    ]
