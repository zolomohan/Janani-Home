# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-04 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20180403_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='multiple_needs',
            field=models.BooleanField(default=False, help_text='Select to allow this user to create multiple needs with separate photo and contact information per need.', verbose_name='Can create multiple needs'),
        ),
    ]