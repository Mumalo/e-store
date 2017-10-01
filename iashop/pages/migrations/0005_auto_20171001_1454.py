# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20170929_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='fb_url',
            field=models.URLField(help_text='use this option for home page only', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pages',
            name='instagram_url',
            field=models.URLField(help_text='use this option for home page only', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pages',
            name='twitter_url',
            field=models.URLField(help_text='use this option for home page only', blank=True, null=True),
        ),
    ]
