from django.contrib import admin
from .models import IGPost, Comment, Like

# Register your models here.
admin.site.register(IGPost)
admin.site.register(Comment)
admin.site.register(Like)
