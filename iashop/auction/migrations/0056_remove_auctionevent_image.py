# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0055_auto_20171009_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionevent',
            name='image',
        ),
    ]
