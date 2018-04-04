# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0060_auto_20171022_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionevent',
            name='image',
            field=models.ManyToManyField(blank=True, to='auction.Image'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.CharField(choices=[(500.0, 'first'), (1000.0, 'second')], max_length=40, blank=True),
        ),
    ]
