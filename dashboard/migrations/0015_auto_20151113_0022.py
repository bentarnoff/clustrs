# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20151112_2103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nugget',
            options={'ordering': ['-votes']},
        ),
        migrations.AlterField(
            model_name='nugget',
            name='read_time',
            field=models.IntegerField(),
        ),
    ]
