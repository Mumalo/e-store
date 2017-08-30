# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0022_auto_20170823_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionevent',
            name='sub_category',
        ),
    ]
