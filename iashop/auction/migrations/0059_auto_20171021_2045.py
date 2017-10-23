# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0058_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionevent',
            name='image',
            field=models.ForeignKey(to='auction.Image', null=True, blank=True),
        ),
    ]
