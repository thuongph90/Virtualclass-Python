# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-27 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0007_register_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='result',
            field=models.TextField(default=None),
        ),
    ]