# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-04 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalwebsite',
            name='social_media_facebook',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='social_media_github',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='social_media_instagram',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='social_media_linkedin',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='social_media_stack_overflow',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='social_media_twitter',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='personalwebsite',
            name='category',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='personalwebsite',
            name='location',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='personalwebsite',
            name='name',
            field=models.CharField(max_length=2000),
        ),
    ]
