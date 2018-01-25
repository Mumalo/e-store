# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20180125_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='title',
            field=models.CharField(max_length=50, unique=True, null=True, default='our profile'),
        ),
    ]
