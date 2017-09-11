# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0034_auto_20170910_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='item',
            new_name='items',
        ),
    ]
