# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0052_auto_20170929_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetplan',
            name='range',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='budgetplan',
            name='time',
            field=models.CharField(null=True, max_length=75, choices=[('YEARS', 'Years'), ('MONTHS', 'Months'), ('WEEKS', 'Weeks'), ('DAYS', 'Days'), ('HOURS', 'Hours'), ('MINUTES', 'Minutes'), ('SECONDS', 'Seconds')]),
        ),
    ]
