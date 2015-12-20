# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20151112_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nugget',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='nugget',
            name='thumbnail_url',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
        ),
    ]
