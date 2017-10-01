# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0048_subcategory2_sub_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'Sub Categories'},
        ),
        migrations.AlterModelOptions(
            name='subcategory2',
            options={'verbose_name_plural': 'Sub Categories 2'},
        ),
        migrations.RemoveField(
            model_name='subcategory2',
            name='category',
        ),
    ]
