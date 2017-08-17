# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auction', '0011_auto_20170817_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionEvent',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('item', models.CharField(null=True, max_length=125)),
                ('target_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('start_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('image', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True, max_length=250)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('bidder', models.ForeignKey(related_name='bids', to=settings.AUTH_USER_MODEL, null=True)),
                ('event', models.ForeignKey(related_name='bids', to='auction.AuctionEvent', null=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.AddField(
            model_name='auctionevent',
            name='category',
            field=models.ForeignKey(to='auction.Category', null=True),
        ),
        migrations.AddField(
            model_name='auctionevent',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
