# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-18 13:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalweb', '0023_auto_20190418_1305'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post_three',
            new_name='PostThree',
        ),
        migrations.RenameModel(
            old_name='Post_two',
            new_name='PostTwo',
        ),
    ]