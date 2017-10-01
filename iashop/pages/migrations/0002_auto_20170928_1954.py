# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, null=True, unique=True, choices=[('Home', 'Home'), ('About', 'About Us'), ('Contact', 'Contact Us')])),
                ('terms', ckeditor_uploader.fields.RichTextUploadingField()),
                ('photos', models.ManyToManyField(to='photologue.Photo', blank=True, help_text='select this option for home page')),
            ],
        ),
        migrations.DeleteModel(
            name='Home',
        ),
    ]
