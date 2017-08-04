from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from base.models import BaseModel
from django.conf import settings
from django.db import models


USER_GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))

class Institution(BaseModel):
    name = models.CharField(max_length=250, blank=False)
    city = models.CharField(max_length=250, blank=False)
    state = models.CharField(max_length=250, blank=False)
    zip_code = models.CharField(blank=True, max_length=25)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile_user')
    photo = models.FileField(verbose_name='profile picture', upload_to='profiles',
                              max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    institution = models.ForeignKey(Institution,
                                    on_delete=models.CASCADE, null=True)
    gender = models.CharField(choices=USER_GENDER_CHOICES, max_length=10, null=True)
    bio = models.TextField(default='', blank=True)


# def create_profile(sender, **kwargs):
#
#     user = kwargs["instance"]
#
#     if kwargs["created"]:
#         user_profile = Profile(user=user)
#         user_profile.save()
#
# post_save.connect(create_profile, sender=User)





