# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0018_auto_20170819_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, null=True, blank=True)),
                ('category', models.ForeignKey(null=True, to='auction.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
