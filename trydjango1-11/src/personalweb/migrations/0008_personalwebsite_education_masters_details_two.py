# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-09 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalweb', '0007_auto_20190409_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalwebsite',
            name='education_masters_details_two',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
