from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser, PermissionsMixin

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class IGPost(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    title = models.CharField(max_length=100)
    image = ProcessedImageField(upload_to='posts',
                                #processors=[ResizeToFill(200,200)],
                                format='JPEG',
                                options={ 'quality': 100})

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('IGPost')
    user = models.OneToOneField(User)
    comment = models.CharField(max_length=100)
