from django.contrib import admin

from .models import Project, Describe, Image, Skill

admin.site.register(Project)
admin.site.register(Describe)
admin.site.register(Image)
admin.site.register(Skill)