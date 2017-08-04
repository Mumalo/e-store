from django.db import models

class BaseModel(models.Model):
    last_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
