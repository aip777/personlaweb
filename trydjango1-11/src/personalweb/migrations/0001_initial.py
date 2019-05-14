# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-02 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalWebsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('location', models.CharField(blank=True, max_length=120, null=True)),
                ('category', models.CharField(blank=True, max_length=120, null=True)),
                ('title', models.CharField(blank=True, max_length=2000, null=True)),
                ('text', models.TextField(blank=True, max_length=2000, null=True)),
                ('experience_title', models.CharField(blank=True, max_length=2000, null=True)),
                ('experience_details', models.TextField(blank=True, max_length=2000, null=True)),
                ('about_title', models.CharField(blank=True, max_length=2000, null=True)),
                ('about_details', models.TextField(blank=True, max_length=2000, null=True)),
                ('skills_title', models.CharField(blank=True, max_length=2000, null=True)),
                ('skills_details', models.TextField(blank=True, max_length=2000, null=True)),
                ('contact_email', models.CharField(blank=True, max_length=2000, null=True)),
                ('contact_address', models.TextField(blank=True, max_length=2000, null=True)),
                ('services_title', models.CharField(blank=True, max_length=2000, null=True)),
                ('services_details', models.TextField(blank=True, max_length=2000, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]