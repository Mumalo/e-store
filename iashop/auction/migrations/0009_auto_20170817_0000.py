# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0008_auto_20170805_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionevent',
            old_name='status',
            new_name='available',
        ),
    ]
