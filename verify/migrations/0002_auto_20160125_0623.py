# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verify',
            old_name='confirmed',
            new_name='access_token',
        ),
        migrations.AddField(
            model_name='verify',
            name='confirm_password',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='verify',
            name='valid',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]