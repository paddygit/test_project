# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 13:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('online_test', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ManyToManyField(related_name='answers', to='online_test.MultipleChoice')),
            ],
        ),
        migrations.CreateModel(
            name='UserResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answer', models.IntegerField(default=0)),
                ('wrong_answer', models.IntegerField(default=0)),
                ('final_score', models.IntegerField(default=0)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_test.Test')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='useranswers',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.UserResult'),
        ),
    ]