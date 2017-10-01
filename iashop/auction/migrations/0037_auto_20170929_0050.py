# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0036_itemoftheday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='price',
            field=models.DecimalField(max_digits=50, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='auctionevent',
            name='current_price',
            field=models.DecimalField(max_digits=50, decimal_places=2, default=0.0),
        ),
        migrations.AlterField(
            model_name='auctionevent',
            name='start_price',
            field=models.DecimalField(max_digits=50, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='auctionevent',
            name='target_price',
            field=models.DecimalField(max_digits=50, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.DecimalField(max_digits=50, decimal_places=2),
        ),
    ]
