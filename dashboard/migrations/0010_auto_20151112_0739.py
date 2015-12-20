# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20151112_0738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nugget',
            name='link',
        ),
        migrations.AddField(
            model_name='nugget',
            name='link_url',
            field=models.URLField(default=None, null=True, blank=True),
        ),
    ]
