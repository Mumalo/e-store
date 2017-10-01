# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0038_auctionevent_place_on_auction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionevent',
            name='place_on_auction',
            field=models.BooleanField(help_text='if you click this you must provide start time, end time, start price and target price', default=False),
        ),
    ]
