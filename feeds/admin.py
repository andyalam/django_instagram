from django.contrib import admin
from .models import UserProfile, IGPost, Comment, Like, Message, Room

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(IGPost)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Message)
admin.site.register(Room)
