# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_auto_20170803_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=2),
        ),
    ]
