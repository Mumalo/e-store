# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0066_budgetplan_budget_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetplan',
            name='budget_image',
            field=models.ImageField(upload_to='budget/%Y/%m/%d', null=True, blank=True),
        ),
    ]
