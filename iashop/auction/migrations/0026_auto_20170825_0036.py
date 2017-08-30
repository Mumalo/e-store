# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0025_auto_20170825_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionevent',
            name='sub_category',
            field=smart_selects.db_fields.ChainedForeignKey(to='auction.SubCategory', chained_model_field='category', auto_choose=True, chained_field='category'),
        ),
    ]
