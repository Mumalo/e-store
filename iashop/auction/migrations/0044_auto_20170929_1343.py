# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0043_auto_20170929_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionevent',
            name='start_price',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
    ]
