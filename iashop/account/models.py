from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from base.models import BaseModel
from django.conf import settings
from django.db import models
from django.utils import timezone

USER_GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))

class Institution(BaseModel):
    name = models.CharField(max_length=250, blank=False)
    city = models.CharField(max_length=250, blank=False)
    state = models.CharField(max_length=250, blank=False)
    zip_code = models.CharField(blank=True, max_length=25)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile_owner')
    photo = models.ImageField(blank=True, null=True, upload_to='profile/users')
    phone = models.CharField(max_length=25, null=True, blank=True)
    institution = models.ForeignKey(Institution,
                                    on_delete=models.CASCADE, null=True)
    gender = models.CharField(choices=USER_GENDER_CHOICES, max_length=10, null=True)
    bio = models.TextField(default='', blank=True)


# Users can follow other users and be followed as well


class Follow(models.Model):
    user_followed = models.ForeignKey(User, related_name='rel_from_set')
    user_following = models.ForeignKey(User, related_name='rel_to_set')

    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)

    class Meta:
        ordering = ('-created',)

following = models.ManyToManyField('self',
                                   through=Follow,
                                   related_name='followers',
                                   symmetrical=False)

User.add_to_class('following',
                  models.ManyToManyField('self',
                                         through=Follow,
                                         related_name='followers',
                                         symmetrical=False
                  )
)






# def create_profile(sender, **kwargs):
#
#     user = kwargs["instance"]
#
#     if kwargs["created"]:
#         user_profile = Profile(user=user)
#         user_profile.save()
#
# post_save.connect(create_profile, sender=User)





