# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-11 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('educational_need', '0004_auto_20170911_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationalneed',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]