# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-05 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_test', '0004_test_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multiplechoice',
            old_name='text',
            new_name='choice_text',
        ),
        migrations.AlterField(
            model_name='multiplechoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_test.Question'),
        ),
    ]