# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-27 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Event title visible in the browser and in search engine results.', max_length=200, verbose_name='Title')),
                ('event_date', models.DateField(default=django.utils.timezone.now, verbose_name='event date')),
                ('description', models.CharField(help_text='Short description of the event.', max_length=200, verbose_name='Short description')),
                ('noindex', models.BooleanField(default=False, help_text='Enable to tell search engine robots to not index this event page.', verbose_name="Don't index this page")),
                ('sorting_value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to='event_images/')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='events.Event')),
            ],
        ),
        migrations.RemoveField(
            model_name='event_image',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event_Image',
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]
