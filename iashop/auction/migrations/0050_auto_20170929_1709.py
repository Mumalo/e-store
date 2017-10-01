# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0049_auto_20170929_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory2',
            name='sub_category',
            field=models.ForeignKey(null=True, related_name='subcat2', to='auction.SubCategory'),
        ),
    ]
