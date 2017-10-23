# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
        ('auction', '0056_remove_auctionevent_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionevent',
            name='image',
            field=models.ForeignKey(null=True, to='photologue.Photo', blank=True),
        ),
    ]
