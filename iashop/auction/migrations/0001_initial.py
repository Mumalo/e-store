# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import django.utils.timezone
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('image1', models.ImageField(upload_to='', blank=True)),
                ('image2', models.ImageField(upload_to='', blank=True)),
                ('image3', models.ImageField(upload_to='', blank=True)),
                ('image4', models.ImageField(upload_to='', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuctionEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('item', models.CharField(max_length=125, null=True)),
                ('target_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('start_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('image', models.ImageField(upload_to='users/%Y/%m/%d', blank=True)),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField(max_length=250, null=True, blank=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2017, 8, 4, 16, 28, 29, 362335, tzinfo=utc), blank=True)),
                ('bidder', models.ForeignKey(related_name='bids', null=True, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(related_name='bids', null=True, to='auction.AuctionEvent')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='auctionevent',
            name='category',
            field=models.ForeignKey(null=True, to='auction.Category'),
        ),
        migrations.AddField(
            model_name='auctionevent',
            name='creator',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
