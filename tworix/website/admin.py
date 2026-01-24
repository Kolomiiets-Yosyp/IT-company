from django.contrib import admin
from .models import Project, Contact, Content, TechStackItem, ProjectMedia

class TechStackItemInline(admin.TabularInline):
    model = TechStackItem
    extra = 1
    fields = ('name', 'description', 'order')
    verbose_name = "Tech Stack Item"
    verbose_name_plural = "Tech Stack Items"

class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia
    extra = 1
    fields = ('media_type', 'image', 'video_url', 'order')
    verbose_name = "Медіа для слайдера"
    verbose_name_plural = "Медіа для слайдера Phase 01"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'description', 'link')
        }),
        ('Фото', {
            'fields': ('image', 'architecture_image'),
            'description': 'image - головне фото (візитка), architecture_image - фото для секції Architecture'
        }),
        ('Візитка проекту (Card)', {
            'fields': ('card_short_description', 'card_button_text'),
            'classes': ('collapse',)
        }),
        ('Intro секція', {
            'fields': ('intro_title', 'intro_description'),
            'classes': ('collapse',)
        }),
        ('Phase 01 - Architecture', {
            'fields': ('phase01_title', 'phase01_subtitle', 'phase01_description', 'phase01_feature1', 'phase01_feature2', 'phase01_button_text'),
            'classes': ('collapse',)
        }),
        ('Phase 02 - Tech Stack', {
            'fields': ('phase02_title', 'phase02_subtitle', 'phase02_description'),
            'classes': ('collapse',)
        }),
        ('Додатково (для сумісності)', {
            'fields': ('details',),
            'classes': ('collapse',)
        }),
    )
    inlines = [TechStackItemInline, ProjectMediaInline]

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    readonly_fields = ('key',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(TechStackItem)
admin.site.register(ProjectMedia)
