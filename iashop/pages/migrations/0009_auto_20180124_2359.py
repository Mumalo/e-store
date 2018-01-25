# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20180124_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('short_intro', models.CharField(max_length=250, blank=True, null=True)),
                ('fb_page_url', models.URLField(blank=True, help_text="link to member's facebook page", null=True)),
                ('tw_page_url', models.URLField(blank=True, help_text="link to member's twitter page", null=True)),
                ('ist_page_url', models.URLField(blank=True, help_text="link to member's instagram page", null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pages',
            name='title',
            field=models.CharField(choices=[('Home', 'Home'), ('About', 'About Us'), ('Contact', 'Contact Us'), ('Make Money', 'Make Money'), ('Partner', 'Partner'), ('Advertise', 'Advertise'), ('Help', 'Help'), ('Terms', 'Terms')], max_length=75, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='ourteam',
            name='team_member',
            field=models.ForeignKey(to='pages.TeamMember', help_text='Add Team Member'),
        ),
    ]
