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
            name='Follow',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('user_followed', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='rel_from_set')),
                ('user_following', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='rel_to_set')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('zip_code', models.CharField(blank=True, max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('photo', models.ImageField(default='static/images/no_image.png', upload_to='profile/users', blank=True, null=True)),
                ('cover', models.ImageField(default='static/images/no_image.png', upload_to='cover/users', blank=True, null=True)),
                ('phone', models.CharField(blank=True, null=True, max_length=25)),
                ('gender', models.CharField(null=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('bio', models.TextField(default='', blank=True)),
                ('institution', models.ForeignKey(null=True, to='account.Institution')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile')),
            ],
        ),
    ]
