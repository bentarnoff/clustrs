# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_nugget_link_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='nugget',
            name='text_or_nah',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='nugget',
            name='clustr',
            field=models.ForeignKey(to='dashboard.Clustr'),
        ),
    ]
