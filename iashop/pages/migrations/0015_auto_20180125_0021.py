# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20180125_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='short_intro',
            field=models.TextField(max_length=250, null=True, blank=True),
        ),
    ]
