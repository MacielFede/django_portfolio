from django.contrib import admin
from .models import PortfolioInfo, Project

class PortfolioInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_position', 'degree_name', 'email')
    search_fields = ('name', 'job_position', 'email')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('title',)

admin.site.register(PortfolioInfo, PortfolioInfoAdmin)
admin.site.register(Project, ProjectAdmin)
