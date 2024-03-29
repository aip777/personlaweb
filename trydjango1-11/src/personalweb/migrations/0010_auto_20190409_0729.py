# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-09 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalweb', '0009_auto_20190409_0709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalwebsite',
            old_name='experience_details',
            new_name='experience_details_five',
        ),
        migrations.RenameField(
            model_name='personalwebsite',
            old_name='experience_title',
            new_name='experience_title_five',
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_details_four',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_details_one',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_details_six',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_details_three',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_details_two',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_title_four',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_title_one',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_title_six',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_title_three',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_title_two',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_years_five',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_years_four',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_years_one',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_years_six',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_years_three',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='personalwebsite',
            name='experience_years_two',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
