# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-27 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0009_auto_20190227_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='result',
            field=models.TextField(default=None, max_length=250, null=True),
        ),
    ]