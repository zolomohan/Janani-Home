# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-29 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20180322_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='organization_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Profile'),
        ),
    ]