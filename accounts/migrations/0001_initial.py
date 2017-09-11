# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-01 18:03
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('educational_need', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='Please use only numeric characters.', regex='^[0-9]*$')])),
                ('hide_mobile_number', models.BooleanField(default=False)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='Please use only numeric characters.', regex='^[0-9]*$')])),
                ('hide_phone_number', models.BooleanField(default=False)),
                ('zip_code', models.CharField(blank=True, max_length=10)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('district', models.CharField(blank=True, max_length=50)),
                ('about', models.TextField(blank=True, max_length=500)),
                ('active_educational_need', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='educational_need.EducationalNeed')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Country')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=2)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Country')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='country', chained_model_field='country', null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.State'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]