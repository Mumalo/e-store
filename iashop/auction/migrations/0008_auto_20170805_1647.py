# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0007_auto_20170805_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
    ]
