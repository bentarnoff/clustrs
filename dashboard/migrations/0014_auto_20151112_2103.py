# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20151112_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nugget',
            name='text_or_nah',
            field=models.NullBooleanField(default=None),
        ),
    ]
