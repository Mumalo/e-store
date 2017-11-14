# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20171019_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='title',
            field=models.CharField(choices=[('Home', 'Home'), ('About', 'About Us'), ('Contact', 'Contact Us'), ('Make Money', 'Make Money'), ('Partner', 'Partner'), ('Advertise', 'Advertise'), ('Help', 'Help'), ('Terms', 'Terms')], null=True, max_length=75, unique=True),
        ),
    ]
