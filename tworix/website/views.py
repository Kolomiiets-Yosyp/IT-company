from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def solutions(request):
    return render(request, 'solutions.html')

def lab(request):
    return render(request, 'lab.html')

def connect(request):
    return render(request, 'connect.html')
