# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20180124_2359'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OurTeam',
            new_name='Team',
        ),
    ]
