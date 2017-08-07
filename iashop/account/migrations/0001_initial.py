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
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('zip_code', models.CharField(max_length=25, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('photo', models.FileField(upload_to='profiles', max_length=255, verbose_name='profile picture', null=True, blank=True)),
                ('phone', models.CharField(max_length=25, null=True, blank=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True)),
                ('bio', models.TextField(default='', blank=True)),
                ('institution', models.ForeignKey(null=True, to='account.Institution')),
                ('user', models.OneToOneField(related_name='profile_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
