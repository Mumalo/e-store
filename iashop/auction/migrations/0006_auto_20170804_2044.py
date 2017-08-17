# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_auto_20170804_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 8, 4, 19, 44, 30, 483482, tzinfo=utc)),
        ),
    ]
