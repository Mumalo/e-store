# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20180124_2359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name_plural': 'Team'},
        ),
    ]
