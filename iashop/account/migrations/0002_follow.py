# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('user_followed', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='rel_from_set')),
                ('user_following', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='rel_to_set')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
