# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_auto_20170804_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 16, 34, 8, 773606, tzinfo=utc), blank=True),
        ),
    ]
