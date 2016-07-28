from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser, PermissionsMixin

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


#class IGUser(AbstractBaseUser, PermissionsMixin):


class IGPost(models.Model):
    image = ProcessedImageField(upload_to='posts',
                                #processors=[ResizeToFill(200,200)],
                                format='JPEG',
                                options={ 'quality': 100})

