# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0023_remove_auctionevent_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionevent',
            name='sub_category',
            field=smart_selects.db_fields.ChainedForeignKey(to='auction.SubCategory', auto_choose=True, default='1', show_all=True, chained_field='category', chained_model_field='category'),
            preserve_default=False,
        ),
    ]
