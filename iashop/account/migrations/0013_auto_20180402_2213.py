# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20180402_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='account.State', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AlterField(
            model_name='lga',
            name='state',
            field=models.ForeignKey(to='account.State', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
    ]
