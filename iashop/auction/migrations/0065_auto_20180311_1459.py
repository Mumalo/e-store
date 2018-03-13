# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0064_auto_20180311_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.IntegerField(choices=[(500, '500.00'), (1000, '100.00')], blank=True),
        ),
    ]
