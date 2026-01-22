from django.contrib import admin
from .models import Project, Contact, Content, ProjectMedia

class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia
    extra = 2
    fields = ('media_type', 'image', 'video_url', 'order')
    verbose_name = "Додаткове медіа"
    verbose_name_plural = "Додаткові медіа"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'description')
    search_fields = ('title', 'description', 'short_description')
    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'image')
        }),
        ('Описи', {
            'fields': ('short_description', 'description'),
            'description': 'short_description - для сторінки /lab/, description - для сторінки проекту'
        }),
        ('Додатково', {
            'fields': ('details', 'link'),
            'classes': ('collapse',)
        }),
    )
    inlines = [ProjectMediaInline]

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    readonly_fields = ('key',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(ProjectMedia)