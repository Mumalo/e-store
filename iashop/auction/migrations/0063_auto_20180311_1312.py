# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0062_auto_20180311_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.CharField(blank=True, max_length=40, choices=[('500.00', 500.0), ('100.00', 1000.0)]),
        ),
    ]
