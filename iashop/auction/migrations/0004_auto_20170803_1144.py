# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_auto_20170803_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionevent',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
