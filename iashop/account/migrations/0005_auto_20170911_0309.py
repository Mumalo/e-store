# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile_agree_to_terms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='agree_to_terms',
            field=models.BooleanField(),
        ),
    ]
