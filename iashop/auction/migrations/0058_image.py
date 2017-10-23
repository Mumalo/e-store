# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import photologue.models


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
        ('auction', '0057_auctionevent_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('image', models.ImageField(upload_to=photologue.models.get_storage_path, verbose_name='image')),
                ('date_taken', models.DateTimeField(help_text='Date image was taken; is obtained from the image EXIF data.', blank=True, verbose_name='date taken', null=True)),
                ('view_count', models.PositiveIntegerField(editable=False, verbose_name='view count', default=0)),
                ('crop_from', models.CharField(choices=[('top', 'Top'), ('right', 'Right'), ('bottom', 'Bottom'), ('left', 'Left'), ('center', 'Center (Default)')], blank=True, verbose_name='crop from', default='center', max_length=10)),
                ('effect', models.ForeignKey(blank=True, to='photologue.PhotoEffect', related_name='image_related', verbose_name='effect', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
