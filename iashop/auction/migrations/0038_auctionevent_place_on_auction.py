# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0037_auto_20170929_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionevent',
            name='place_on_auction',
            field=models.BooleanField(default=False),
        ),
    ]
