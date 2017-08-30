# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0019_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionevent',
            name='sub_category',
            field=models.ForeignKey(to='auction.SubCategory', null=True, blank=True),
        ),
    ]
