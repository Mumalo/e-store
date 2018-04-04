# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20180403_0035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='local_govt_area',
            new_name='lga',
        ),
    ]
