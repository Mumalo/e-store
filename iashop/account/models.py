from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from base.models import BaseModel
from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

USER_GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
DEFAULT_COVER = ('default/default_cover.png')
DEFAULT_PROFILE = ('default/default_profile.png')

class Institution(BaseModel):
    name = models.CharField(max_length=250, blank=False)
    city = models.CharField(max_length=250, blank=False)
    state = models.CharField(max_length=250, blank=False)
    zip_code = models.CharField(blank=True, max_length=25)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    photo = models.ImageField(blank=True, null=True, upload_to='profile/users', default=DEFAULT_PROFILE)
    # cover = models.ImageField(blank=True, null=True, upload_to='cover/users', default=DEFAULT_COVER)
    phone = models.CharField(max_length=25, null=True, blank=True, default='00000000')
    institution = models.ForeignKey(Institution,
                                    on_delete=models.CASCADE, null=True)
    agree_to_terms = models.BooleanField(default=False)

    gender = models.CharField(choices=USER_GENDER_CHOICES, max_length=10, null=True)
    bio = models.TextField(default='', blank=True)

# Create signal to create profile model each time a new user is created

def create_profle(sender, **kwargs):
    user = kwargs['instance']
    if kwargs['created']:
        user_profile = Profile(user=user)
        user_profile.save()

post_save.connect(create_profle, sender=User)

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





