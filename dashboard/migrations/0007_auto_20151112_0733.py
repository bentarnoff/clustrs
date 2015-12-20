# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_nugget_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nugget',
            name='url',
            field=models.URLField(),
        ),
    ]
