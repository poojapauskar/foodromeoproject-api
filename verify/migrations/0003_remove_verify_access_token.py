# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 05:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0002_auto_20160125_0623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verify',
            name='access_token',
        ),
    ]