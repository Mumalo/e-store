# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0010_auto_20170817_0001'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Advert',
        ),
        migrations.RemoveField(
            model_name='auctionevent',
            name='category',
        ),
        migrations.RemoveField(
            model_name='auctionevent',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='bidder',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='event',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
        migrations.DeleteModel(
            name='AuctionEvent',
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
