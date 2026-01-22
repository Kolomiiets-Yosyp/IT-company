from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(blank=True, default="", help_text="Короткий опис для відображення на сторінці /lab/")
    description = models.TextField(help_text="Повний опис для відображення на сторінці проекту")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Головне фото (візитка) для відображення на /lab/")
    details = models.TextField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class ProjectMedia(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Фото'),
        ('video', 'Відео'),
    ]
    
    project = models.ForeignKey(Project, related_name='media', on_delete=models.CASCADE)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='image')
    image = models.ImageField(upload_to='projects/media/', blank=True, null=True, help_text="Фото (якщо media_type = image)")
    video_url = models.URLField(blank=True, null=True, help_text="URL відео (YouTube, Vimeo тощо) - якщо media_type = video")
    order = models.IntegerField(default=0, help_text="Порядок відображення")

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
