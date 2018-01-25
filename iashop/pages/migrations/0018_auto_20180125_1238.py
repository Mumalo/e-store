# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20180125_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_member',
        ),
        migrations.AddField(
            model_name='teammember',
            name='team',
            field=models.ForeignKey(help_text='Add Team', to='pages.Team', null=True),
        ),
    ]
