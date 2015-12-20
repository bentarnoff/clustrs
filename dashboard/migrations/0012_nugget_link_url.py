# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_remove_nugget_link_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='nugget',
            name='link_url',
            field=models.URLField(default=None, null=True, blank=True),
        ),
    ]
