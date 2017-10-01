# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0045_auto_20170929_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionevent',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='auctionevent',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
