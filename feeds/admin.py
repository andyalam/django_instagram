from django.contrib import admin
from .models import UserProfile, IGPost, Comment, Like

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(IGPost)
admin.site.register(Comment)
admin.site.register(Like)
