# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-04 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalweb', '0002_auto_20190404_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalwebsite',
            name='contact_number',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='personalwebsite',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personalwebsite',
            name='contact_address',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='personalwebsite',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='personalwebsite',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='personalwebsite',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
