from django.contrib import admin
from .models import Project, Contact, Content

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    readonly_fields = ('key',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Content, ContentAdmin)