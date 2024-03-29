# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-29 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalweb', '0035_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_image',
            new_name='bg_image',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_title_four',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_title_one',
            new_name='client_number',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_title_three',
            new_name='coffee',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_title_two',
            new_name='coffee_number',
        ),
        migrations.AddField(
            model_name='client',
            name='partners',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='partners_number',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='projects',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='projects_number',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
