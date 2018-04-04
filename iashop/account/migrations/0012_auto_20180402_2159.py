# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20180402_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='cities_loaded',
            new_name='city_loaded',
        ),
        migrations.RenameField(
            model_name='lga',
            old_name='lgas_loaded',
            new_name='lga_loaded',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='states_loaded',
            new_name='state_loaded',
        ),
    ]
