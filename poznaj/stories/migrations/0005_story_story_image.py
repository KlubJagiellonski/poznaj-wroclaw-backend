# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_copyright'),
        ('stories', '0004_story_first_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='story_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='story_image', to='images.Image'),
        ),
    ]
