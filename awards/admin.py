from django.contrib import admin

from .models import Profile, Comment, Rate, Project

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Rate)
