# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_team_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='title',
            field=models.CharField(unique=True, max_length=50, null=True, default='our team'),
        ),
    ]
