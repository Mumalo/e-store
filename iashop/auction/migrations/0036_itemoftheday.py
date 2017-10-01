# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auction', '0035_auto_20170910_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemOfTheDay',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(help_text='Please select a category to include', blank=True, to='auction.Category', null=True)),
                ('subcategory', models.ForeignKey(help_text='Please select select a sub category to include', blank=True, to='auction.SubCategory', null=True)),
                ('user', models.ForeignKey(help_text='Please select a user whose items you wish to include', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Item of the day',
                'verbose_name_plural': 'Items of the day',
            },
        ),
    ]
