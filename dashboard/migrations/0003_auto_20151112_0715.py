# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20151112_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clustr',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nugget',
            name='author',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nugget',
            name='read_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='nugget',
            name='source',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nugget',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nugget',
            name='votes',
            field=models.IntegerField(),
        ),
    ]
