# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0015_auto_20151113_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cred', models.IntegerField()),
                ('active_clustrs', models.ManyToManyField(to='dashboard.Clustr')),
                ('contributions', models.ManyToManyField(related_name='contributed_nuggets', to='dashboard.Nugget')),
                ('queue', models.ManyToManyField(related_name='nuggets_in_queue', to='dashboard.Nugget')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
