# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20171023_2154'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Institution',
            new_name='State',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='institution',
            new_name='state',
        ),
    ]
