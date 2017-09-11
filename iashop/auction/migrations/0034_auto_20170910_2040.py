# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0033_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='item',
            field=models.ManyToManyField(to='auction.AuctionEvent'),
        ),
    ]
