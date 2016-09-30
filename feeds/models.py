from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser, PermissionsMixin

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    followers = models.ManyToManyField('UserProfile',
                                        related_name="followers_profile",
                                        null=True,
                                        blank=True)
    following = models.ManyToManyField('UserProfile',
                                        related_name="following_profile",
                                        null=True,
                                        blank=True)

class IGPost(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    profile = models.ForeignKey(UserProfile, null=True, blank=True)
    title = models.CharField(max_length=100)
    image = ProcessedImageField(upload_to='posts',
                                #processors=[ResizeToFill(200,200)],
                                format='JPEG',
                                options={ 'quality': 100})
    posted_on = models.DateTimeField()

    def get_number_of_likes(self):
        return self.like_set.count()

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('IGPost')
    user = models.OneToOneField(User)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField()


class Like(models.Model):
    post = models.ForeignKey('IGPost')
    user = models.OneToOneField(User)
