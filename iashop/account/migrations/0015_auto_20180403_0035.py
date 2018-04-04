# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20180402_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='lga',
        ),
        migrations.AddField(
            model_name='profile',
            name='local_govt_area',
            field=models.ForeignKey(to='account.Lga', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
    ]
