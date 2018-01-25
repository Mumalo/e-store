# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
        ('pages', '0013_team_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='photo',
        ),
        migrations.AddField(
            model_name='teammember',
            name='photo',
            field=models.ForeignKey(to='photologue.Photo', null=True),
        ),
    ]
