# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0017_auto_20170819_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='event',
            field=models.ForeignKey(to='auction.AuctionEvent', related_name='bids', null=True),
        ),
    ]
