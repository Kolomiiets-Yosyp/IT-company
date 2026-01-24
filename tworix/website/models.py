from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Головне фото (візитка) для картки проекту")
    architecture_image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Фото для секції Architecture (внизу)")
    
    # Card (візитка) поля
    card_short_description = models.TextField(blank=True, default="", help_text="Короткий опис для візитки проекту")
    card_button_text = models.CharField(max_length=50, blank=True, default="View Project", help_text="Текст кнопки на візитці")
    
    # Intro секція
    intro_title = models.CharField(max_length=200, blank=True, default="", help_text="Заголовок intro секції (якщо порожнє, використовується назва проекту)")
    intro_description = models.TextField(blank=True, default="", help_text="Опис для intro секції (якщо порожнє, використовується description)")
    
    # Phase 01 (Architecture)
    phase01_title = models.CharField(max_length=100, blank=True, default="Phase 01", help_text="Заголовок Phase 01")
    phase01_subtitle = models.CharField(max_length=200, blank=True, default="PROJECT OVERVIEW", help_text="Підзаголовок Phase 01")
    phase01_description = models.TextField(blank=True, default="", help_text="Опис Phase 01 (якщо порожнє, використовується details)")
    phase01_feature1 = models.CharField(max_length=200, blank=True, default="High-Performance Architecture", help_text="Перша перевага")
    phase01_feature2 = models.CharField(max_length=200, blank=True, default="Modern Development Stack", help_text="Друга перевага")
    phase01_button_text = models.CharField(max_length=50, blank=True, default="Explore Project", help_text="Текст кнопки Phase 01")
    
    # Phase 02 (Tech Stack)
    phase02_title = models.CharField(max_length=100, blank=True, default="Phase 02", help_text="Заголовок Phase 02")
    phase02_subtitle = models.CharField(max_length=200, blank=True, default="TECH STACK", help_text="Підзаголовок Phase 02")
    phase02_description = models.TextField(blank=True, default="Built on a foundation of reliability and scale. Our choice of technologies reflects a commitment to a developer-first experience and lightning-fast performance across all platforms.", help_text="Опис Phase 02")
    
    # Старі поля (для сумісності)
    details = models.TextField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class TechStackItem(models.Model):
    project = models.ForeignKey(Project, related_name='tech_stack_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="Назва технології")
    description = models.CharField(max_length=200, help_text="Опис технології")
    order = models.IntegerField(default=0, help_text="Порядок відображення")

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.project.title} - {self.name}"

class ProjectMedia(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Фото'),
        ('video', 'Відео'),
    ]
    
    project = models.ForeignKey(Project, related_name='media_items', on_delete=models.CASCADE)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='image')
    image = models.ImageField(upload_to='projects/media/', blank=True, null=True, help_text="Фото (якщо media_type = image)")
    video_url = models.URLField(blank=True, null=True, help_text="URL відео (YouTube, Vimeo тощо) - якщо media_type = video. Використовуйте embed URL")
    order = models.IntegerField(default=0, help_text="Порядок відображення в слайдері")

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.project.title} - {self.get_media_type_display()} #{self.order}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Content(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key
