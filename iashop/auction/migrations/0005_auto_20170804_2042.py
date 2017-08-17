# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_auto_20170804_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 19, 42, 29, 181229, tzinfo=utc), blank=True),
        ),
    ]
