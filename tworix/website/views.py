from django.shortcuts import render, get_object_or_404
from .models import Project, Contact
from django.http import JsonResponse

def index(request):
    latest_projects = Project.objects.order_by('-id')[:3] # Get latest 3 projects
    return render(request, 'index.html', {'latest_projects': latest_projects})

def solutions(request):
    return render(request, 'solutions.html')

def lab(request):
    projects = Project.objects.all()
    return render(request, 'lab.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def connect(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            return JsonResponse({'success': True, 'message': 'Thank you for your message!'})
        else:
            return JsonResponse({'success': False, 'message': 'Please fill in all fields.'})

    return render(request, 'connect.html')
