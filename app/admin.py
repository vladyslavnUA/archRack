from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','slug', 'owner', 'created_at', 'updated_at',]

    def get_collabs(self, obj):
        return "\n".join([p.collaborators for p in obj.collaborators.all()])

    def get_docs(self, obj):
        return "\n".join([p.rackdocs for p in obj.rackdocs.all()])

class RackDocAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'owner', 'created_at', 'updated_at',]

admin.site.register(Project, ProjectAdmin)
admin.site.register(RackDoc, RackDocAdmin)