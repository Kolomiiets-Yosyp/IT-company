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

def about(request):
    context = get_content_context()
    return render(request, 'about.html', context)

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

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            return JsonResponse({'success': True, 'message': 'Your message has been sent successfully!'})
        else:
            return JsonResponse({'success': False, 'message': 'Please fill all the required fields.'})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})
