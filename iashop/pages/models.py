from django.db import models


from photologue.models import Gallery, Photo
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Pages(models.Model):

    HOME_CHOICES = (
        ('Home', 'Home'),
        ('About', 'About Us'),
        ('Contact', 'Contact Us'),
        ('Make Money', 'Make Money'),
        ('Partner', 'Partner'),
        ('Advertise', 'Advertise'),
        ('Help', 'Help'),
        ('Terms', 'Terms'),
    )

    title = models.CharField(choices=HOME_CHOICES, max_length=75, unique=True, null=True)
    photos = models.ManyToManyField(Photo, blank=True, help_text='select this option for home page')
    text = RichTextUploadingField()
    fb_url = models.URLField(null=True, blank=True, help_text='use this option for home page only')
    instagram_url = models.URLField(null=True, blank=True, help_text='use this option for home page only')
    twitter_url = models.URLField(null=True, blank=True, help_text='use this option for home page only')

    class Meta:
        verbose_name_plural = 'Page'

    def __str__(self):
        return self.title

#
# Temporal implementation of the company team page
# #

class Team(models.Model):
    title = models.CharField(max_length=50, unique=True, null=True, default='our team')

    class Meta:
        verbose_name_plural = 'Team'

    def __str__(self):
        return "company profile"

class TeamMember(models.Model):
    short_intro = models.TextField(max_length=250, null=True, blank=True)
    photo = models.ForeignKey(Photo, null=True, on_delete=models.CASCADE)
    fb_page_url = models.URLField(null=True, blank=True, help_text="link to member\'s facebook page")
    tw_page_url = models.URLField(null=True, blank=True, help_text="link to member\'s twitter page")
    inst_page_url = models.URLField(null=True, blank=True, help_text="link to member\'s instagram page")
    name = models.CharField(max_length=150, null=True)
    position = models.CharField(max_length=150, null=True)
    team = models.ForeignKey(Team, help_text='Add Team', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



# Create your models here.
