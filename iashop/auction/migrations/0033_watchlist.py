# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auction', '0032_auto_20170906_0101'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
                ('item', models.ManyToManyField(null=True, to='auction.AuctionEvent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
