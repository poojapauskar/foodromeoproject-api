# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_register_activation_key_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='is_set_pw',
            field=models.CharField(blank=True, default=b'', max_length=100),
        ),
    ]
