# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_auto_20170804_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 5, 15, 46, 6, 173954, tzinfo=utc), blank=True),
        ),
    ]
