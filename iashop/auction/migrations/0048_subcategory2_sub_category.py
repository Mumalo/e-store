# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0047_auto_20170929_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory2',
            name='sub_category',
            field=models.ForeignKey(null=True, to='auction.SubCategory'),
        ),
    ]
