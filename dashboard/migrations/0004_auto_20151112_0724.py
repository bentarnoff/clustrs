# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20151112_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nugget',
            name='read_time',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
    ]
