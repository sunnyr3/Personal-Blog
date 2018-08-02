# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 11:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simplemde.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_auto_20170225_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=simplemde.fields.SimpleMDEField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='body',
            field=simplemde.fields.SimpleMDEField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
