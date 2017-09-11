# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170817_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='agree_to_terms',
            field=models.BooleanField(default=False),
        ),
    ]
