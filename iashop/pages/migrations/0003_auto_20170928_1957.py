# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20170928_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pages',
            old_name='terms',
            new_name='text',
        ),
    ]
