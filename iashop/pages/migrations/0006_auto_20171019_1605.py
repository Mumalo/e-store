# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20171001_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='title',
            field=models.CharField(max_length=75, unique=True, null=True, choices=[('Home', 'Home'), ('About', 'About Us'), ('Contact', 'Contact Us'), ('Make Money', 'Make Money'), ('Partner', 'Partner'), ('Advertise', 'Advertise'), ('Help', 'Help')]),
        ),
    ]
