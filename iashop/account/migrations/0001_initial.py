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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(max_length=255, verbose_name='profile picture', blank=True, upload_to='profiles', null=True)),
                ('phone', models.CharField(max_length=25, blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True)),
                ('bio', models.TextField(blank=True, default='')),
                ('institution', models.ForeignKey(to='account.Institution', null=True)),
                ('user', models.OneToOneField(related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
