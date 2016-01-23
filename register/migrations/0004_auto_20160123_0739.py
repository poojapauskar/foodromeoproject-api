# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20160123_0606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='fb_token',
            new_name='fb_id',
        ),
        migrations.AddField(
            model_name='register',
            name='google_access_token',
            field=models.CharField(blank=True, default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='register',
            name='google_id',
            field=models.CharField(blank=True, default=b'', max_length=100),
        ),
    ]
