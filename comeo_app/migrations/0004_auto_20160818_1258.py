# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-18 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comeo_app', '0003_auto_20160328_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comeouser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='comeouser',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='comeouser',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='campaign',
            name='desc_headline',
            field=models.CharField(max_length=300, verbose_name='Campaign headline'),
        ),
        migrations.DeleteModel(
            name='ComeoUser',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]