# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionevent',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d'),
        ),
    ]
