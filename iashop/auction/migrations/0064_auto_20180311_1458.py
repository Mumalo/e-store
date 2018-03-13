# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0063_auto_20180311_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.IntegerField(blank=True, choices=[(500, 'first'), (1000, 'second')]),
        ),
    ]
