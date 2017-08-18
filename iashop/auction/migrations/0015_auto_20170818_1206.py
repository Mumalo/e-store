# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auction', '0014_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('last_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(null=True, max_length=250)),
                ('image', models.ImageField(null=True, upload_to='users/advert', blank=True)),
                ('description', models.TextField(null=True, max_length=500, blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'ordering': ('-last_created',),
            },
        ),
        migrations.CreateModel(
            name='BudgetPlan',
            fields=[
                ('advert_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, to='auction.Advert', serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('auction.advert',),
        ),
        migrations.AddField(
            model_name='advert',
            name='creator',
            field=models.ForeignKey(related_name='advert', to=settings.AUTH_USER_MODEL),
        ),
    ]
