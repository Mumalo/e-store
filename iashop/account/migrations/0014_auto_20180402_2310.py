# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20180402_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='lga',
            field=models.ForeignKey(null=True, to='account.Lga', on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.ForeignKey(null=True, to='account.State', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
