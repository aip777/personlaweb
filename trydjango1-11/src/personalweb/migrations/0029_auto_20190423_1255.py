# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-23 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalweb', '0028_auto_20190423_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_masters', models.CharField(blank=True, max_length=2000, null=True)),
                ('education_masters_details', models.TextField(blank=True, max_length=2000, null=True)),
                ('education_masters_details_two', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='education_masters',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='education_masters_details',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='education_masters_details_two',
        ),
    ]
