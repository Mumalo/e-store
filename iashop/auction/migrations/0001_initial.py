# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('item', models.CharField(max_length=125, null=True)),
                ('target_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('start_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField(max_length=250, blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('bidder', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('event', models.ForeignKey(to='auction.AuctionEvent', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
