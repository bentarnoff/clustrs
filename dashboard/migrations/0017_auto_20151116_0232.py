# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='active_clustrs',
            field=models.ManyToManyField(default=None, to='dashboard.Clustr', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='contributions',
            field=models.ManyToManyField(default=None, related_name='contributed_nuggets', to='dashboard.Nugget', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cred',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='queue',
            field=models.ManyToManyField(default=None, related_name='nuggets_in_queue', to='dashboard.Nugget', blank=True),
        ),
    ]
