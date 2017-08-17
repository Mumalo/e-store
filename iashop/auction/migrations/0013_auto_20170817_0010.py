# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0012_auto_20170817_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionevent',
            old_name='status',
            new_name='available',
        ),
    ]
