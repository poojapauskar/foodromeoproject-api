# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(blank=True, default=b'', max_length=100),
        ),
    ]
