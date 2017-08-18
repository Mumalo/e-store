# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0015_auto_20170818_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
