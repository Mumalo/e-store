# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0009_auto_20170817_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionevent',
            old_name='available',
            new_name='status',
        ),
    ]
