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
    profile_pic = ProcessedImageField(upload_to='profile_pics',
                                format='JPEG',
                                options={ 'quality': 100},
                                null=True,
                                blank=True)

    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username

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

    def get_number_of_comments(self):
        return self.comment_set.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('IGPost')
    user = models.OneToOneField(User)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField()

    def __str__(self):
        return self.comment


class Like(models.Model):
    post = models.ForeignKey('IGPost')
    user = models.OneToOneField(User)

    def __str__(self):
        return 'Like: ' + self.user.username + ' ' + self.post.title
