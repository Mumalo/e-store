# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0016_advert_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='time_frame',
            field=models.CharField(null=True, max_length=125),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(null=True, related_name='bidder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bid',
            name='event',
            field=models.ForeignKey(null=True, related_name='event', to='auction.AuctionEvent'),
        ),
    ]
