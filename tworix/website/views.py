from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Project, Contact, Content
from django.http import JsonResponse

def get_content_context():
    content = Content.objects.all()
    context = {item.key: item.value for item in content}
    return context

class BuildView(TemplateView):
    template_name = "build.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_content_context())
        return context

class GridView(TemplateView):
    template_name = "grid.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_content_context())
        return context

class CoreView(TemplateView):
    template_name = "core.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_content_context())
        return context

class DirectoryView(TemplateView):
    template_name = "directory.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_content_context())
        return context

class TheVaultView(TemplateView):
    template_name = "the_vault.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_content_context())
        return context

class NodesView(TemplateView):
    template_name = "nodes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_content_context())
        return context

def index(request):
    context = get_content_context()
    context['latest_projects'] = Project.objects.order_by('-id')[:3]
    return render(request, 'index.html', context)

def solutions(request):
    context = get_content_context()
    return render(request, 'solutions.html', context)

def rules(request):
    context = get_content_context()
    return render(request, 'rules.html', context)

def lab(request):
    context = get_content_context()
    context['projects'] = Project.objects.all()
    return render(request, 'lab.html', context)

def project_detail(request, pk):
    context = get_content_context()
    context['project'] = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', context)

def connect(request):
    context = get_content_context()
    return render(request, 'connect.html', context)

from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings


def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            # Збереження в базу (якщо потрібно)
            # Contact.objects.create(name=name, email=email, message=message)

            subject = "New message from TWORIX"

            # Звичайний текст для поштових клієнтів, які не підтримують HTML
            plain_message = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

            # Гарний HTML-шаблон листа зі стилями (шрифти, відступи, кольори)
            html_message = f"""
            <html>
                <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; padding: 20px; color: #333;">
                    <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">

                        <h2 style="color: #2c3e50; border-bottom: 2px solid #007bff; padding-bottom: 10px; margin-top: 0;">
                            Нове повідомлення з сайту
                        </h2>

                        <p style="font-size: 16px; margin-bottom: 5px;">
                            <strong style="color: #555;">Ім'я:</strong> {name}
                        </p>

                        <p style="font-size: 16px; margin-bottom: 20px;">
                            <strong style="color: #555;">Email:</strong> 
                            <a href="mailto:{email}" style="color: #007bff; text-decoration: none;">{email}</a>
                        </p>

                        <p style="font-size: 14px; color: #777; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 1px;">
                            Текст повідомлення:
                        </p>

                        <div style="background-color: #f9f9f9; padding: 15px; border-left: 4px solid #007bff; border-radius: 4px; font-size: 16px; font-style: italic; color: #444;">
                            {message}
                        </div>

                        <p style="margin-top: 30px; font-size: 12px; color: #aaa; text-align: center; border-top: 1px solid #eee; padding-top: 15px;">
                            Це автоматичне повідомлення від системи TWORIX. Будь ласка, не відповідайте на цей лист напряму, використовуйте email клієнта.
                        </p>

                    </div>
                </body>
            </html>
            """

            try:
                send_mail(
                    subject=subject,
                    message=plain_message,  # Fallback для старих клієнтів
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['tworix.company@gmail.com'],
                    html_message=html_message,  # Передаємо наш гарний дизайн сюди
                    fail_silently=False,
                )
                return JsonResponse({'success': True, 'message': 'Your message has been sent successfully!'})
            except Exception as e:
                print(f"Error sending email: {e}")
                return JsonResponse({'success': False, 'message': 'Failed to send email.'})
        else:
            return JsonResponse({'success': False, 'message': 'Please fill all the required fields.'})

    return JsonResponse({'success': False, 'message': 'Invalid request.'})