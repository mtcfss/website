# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 11:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0018_auto_20161103_1109'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inscription',
            unique_together=set([('member', 'session')]),
        ),
    ]
