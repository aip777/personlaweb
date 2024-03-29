# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-23 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalweb', '0027_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_title_one', models.CharField(blank=True, max_length=2000, null=True)),
                ('experience_years_one', models.CharField(blank=True, max_length=2000, null=True)),
                ('experience_details_one', models.TextField(blank=True, max_length=2000, null=True)),
                ('experience_title_two', models.CharField(blank=True, max_length=2000, null=True)),
                ('experience_years_two', models.CharField(blank=True, max_length=2000, null=True)),
                ('experience_details_two', models.TextField(blank=True, max_length=2000, null=True)),
                ('experience_title_three', models.CharField(blank=True, max_length=2000, null=True)),
                ('experience_years_three', models.CharField(blank=True, max_length=2000, null=True)),
                ('experience_details_three', models.TextField(blank=True, max_length=2000, null=True)),
                ('experience_title_four', models.CharField(blank=True, max_length=2000, null=True)),
                ('experience_years_four', models.CharField(blank=True, max_length=2000, null=True)),
                ('experience_details_four', models.TextField(blank=True, max_length=2000, null=True)),
                ('experience_title_five', models.CharField(blank=True, max_length=2000, null=True)),
                ('experience_years_five', models.CharField(blank=True, max_length=2000, null=True)),
                ('experience_details_five', models.TextField(blank=True, max_length=2000, null=True)),
                ('experience_title_six', models.CharField(blank=True, max_length=2000, null=True)),
                ('experience_years_six', models.CharField(blank=True, max_length=2000, null=True)),
                ('experience_details_six', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_details_five',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_details_four',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_details_one',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_details_six',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_details_three',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_details_two',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_title_five',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_title_four',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_title_one',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_title_six',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_title_three',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_title_two',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_years_five',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_years_four',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_years_one',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_years_six',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_years_three',
        ),
        migrations.RemoveField(
            model_name='personalwebsite',
            name='experience_years_two',
        ),
    ]
