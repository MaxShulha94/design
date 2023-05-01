from django.contrib import admin
from .models import ProjectCategory, Project, Contact, Team, AboutGallery


admin.site.register(Contact)
admin.site.register(Team)
admin.site.register(AboutGallery)


@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ['position', 'client_name', 'category_name', 'text', 'project_name', 'description', 'category']


@admin.register(ProjectCategory)
class ProjectCategory(admin.ModelAdmin):
    list_display = ['position', 'client_name', 'category_name' ]
    list_editable = ['client_name', 'category_name']