# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0026_auto_20170825_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionevent',
            name='sub_category',
            field=models.ForeignKey(null=True, to='auction.SubCategory', blank=True),
        ),
    ]
