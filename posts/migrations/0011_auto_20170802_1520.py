# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-02 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_loke'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Loke',
            new_name='Like',
        ),
    ]