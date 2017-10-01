# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0041_auto_20170929_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionevent',
            name='place_on_auction',
            field=models.NullBooleanField(help_text='if you click this you must provide start time, end time, start price and target price', default=False),
        ),
    ]
