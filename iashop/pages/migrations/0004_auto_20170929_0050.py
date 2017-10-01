# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20170928_1957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pages',
            options={'verbose_name_plural': 'Page'},
        ),
    ]
