# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0028_auto_20170825_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionevent',
            name='category',
            field=models.ForeignKey(related_name='cat_products', null=True, to='auction.Category'),
        ),
        migrations.AlterField(
            model_name='auctionevent',
            name='sub_category',
            field=models.ForeignKey(related_name='sub_products', blank=True, null=True, to='auction.SubCategory'),
        ),
    ]
