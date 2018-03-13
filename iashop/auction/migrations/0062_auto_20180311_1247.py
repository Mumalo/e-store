# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0061_auto_20180311_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.CharField(blank=True, choices=[('first', 500.0), ('second', 1000.0)], max_length=40),
        ),
    ]
