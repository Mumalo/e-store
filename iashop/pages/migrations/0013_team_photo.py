# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
        ('pages', '0012_auto_20180125_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='photo',
            field=models.ForeignKey(null=True, to='photologue.Photo', on_delete=models.CASCADE),
        ),
    ]
