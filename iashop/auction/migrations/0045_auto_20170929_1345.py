# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0044_auto_20170929_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionevent',
            name='start_price',
            field=models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=50),
        ),
    ]
