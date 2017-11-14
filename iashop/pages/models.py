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





# Create your models here.
