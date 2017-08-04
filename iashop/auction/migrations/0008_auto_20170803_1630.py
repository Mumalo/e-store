# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0007_auto_20170803_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 8, 3, 15, 30, 5, 312596, tzinfo=utc)),
        ),
    ]
