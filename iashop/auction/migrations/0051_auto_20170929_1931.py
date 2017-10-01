# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0050_auto_20170929_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=250, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=250, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory2',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
