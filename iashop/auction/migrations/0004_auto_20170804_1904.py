# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_auto_20170804_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 8, 4, 18, 4, 45, 131634, tzinfo=utc)),
        ),
    ]
