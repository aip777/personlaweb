# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-09 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalweb', '0004_personalwebsite_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalwebsite',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]
