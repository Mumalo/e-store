# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_auto_20170803_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='bids', null=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='event',
            field=models.ForeignKey(to='auction.AuctionEvent', related_name='bids', null=True),
        ),
    ]
