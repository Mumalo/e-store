# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0046_auto_20170929_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, null=True)),
                ('category', models.ForeignKey(related_name='subcat2', null=True, to='auction.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='auctionevent',
            name='sub_category2',
            field=models.ForeignKey(null=True, to='auction.SubCategory2', related_name='sub_products2', blank=True),
        ),
    ]
