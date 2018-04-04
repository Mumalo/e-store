# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0065_auto_20180311_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetplan',
            name='budget_image',
            field=models.ImageField(null=True, upload_to='budget/%Y/%m/%d'),
        ),
    ]
