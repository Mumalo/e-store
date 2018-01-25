# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20180125_0008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammember',
            old_name='ist_page_url',
            new_name='inst_page_url',
        ),
        migrations.AddField(
            model_name='teammember',
            name='name',
            field=models.CharField(null=True, max_length=150),
        ),
        migrations.AddField(
            model_name='teammember',
            name='position',
            field=models.CharField(null=True, max_length=150),
        ),
    ]
