# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nugget',
            name='clustr',
            field=models.ForeignKey(default=None, to='dashboard.Clustr'),
        ),
        migrations.AlterField(
            model_name='nugget',
            name='author',
            field=models.TextField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nugget',
            name='source',
            field=models.TextField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nugget',
            name='thumbnail_text',
            field=models.TextField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nugget',
            name='thumbnail_url',
            field=models.URLField(default=None, null=True, blank=True),
        ),
    ]
