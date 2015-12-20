# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clustr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Nugget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('source', models.TextField()),
                ('date', models.DateField()),
                ('thumbnail_text', models.TextField()),
                ('thumbnail_url', models.URLField()),
                ('comment', models.TextField()),
                ('read_time', models.DecimalField(max_digits=5, decimal_places=5)),
                ('contributor', models.CharField(max_length=100)),
                ('votes', models.DecimalField(max_digits=5, decimal_places=5)),
            ],
        ),
    ]
