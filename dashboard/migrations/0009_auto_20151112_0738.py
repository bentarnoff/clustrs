# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20151112_0735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nugget',
            old_name='url',
            new_name='link',
        ),
    ]
