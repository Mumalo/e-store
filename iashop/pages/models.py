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
    )

    title = models.CharField(choices=HOME_CHOICES, max_length=75, unique=True, null=True)
    photos = models.ManyToManyField(Photo, blank=True, help_text='select this option for home page')
    text = RichTextUploadingField()



    class Meta:
        verbose_name_plural = 'Page'

    def __str__(self):
        return self.title





# Create your models here.
