# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_auctionevent_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auctionevent',
            options={'ordering': ('-time',)},
        ),
        migrations.AddField(
            model_name='auctionevent',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 3, 11, 41, 48, 899813)),
        ),
    ]
