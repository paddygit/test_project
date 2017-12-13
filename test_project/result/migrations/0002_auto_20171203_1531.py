# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0001_initial'),
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswers',
            name='answer',
        ),
        migrations.AddField(
            model_name='useranswers',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='online_test.MultipleChoice', verbose_name='Answer'),
        ),
    ]
