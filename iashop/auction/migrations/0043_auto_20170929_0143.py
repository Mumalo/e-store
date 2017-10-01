# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0042_auto_20170929_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionevent',
            name='place_on_auction',
            field=models.NullBooleanField(help_text='if you click this you must provide start time, end time, start price and target price', default=True),
        ),
    ]
