# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20151112_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nugget',
            name='url',
            field=models.URLField(default=None, null=True, blank=True),
        ),
    ]
