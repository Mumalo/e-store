# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0031_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionevent',
            name='current_price',
            field=models.DecimalField(default=0.0, decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='category/%Y/%m/%d'),
        ),
    ]
