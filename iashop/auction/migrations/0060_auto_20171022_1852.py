# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0059_auto_20171021_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionevent',
            name='image',
        ),
        migrations.AddField(
            model_name='auctionevent',
            name='image',
            field=models.ManyToManyField(null=True, blank=True, to='auction.Image'),
        ),
    ]
