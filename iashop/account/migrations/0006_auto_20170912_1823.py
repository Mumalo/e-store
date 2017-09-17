# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20170911_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='agree_to_terms',
            field=models.BooleanField(default=False),
        ),
    ]
