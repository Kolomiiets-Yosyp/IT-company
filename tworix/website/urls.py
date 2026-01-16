from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('solutions/', views.solutions, name='solutions'),
    path('lab/', views.lab, name='lab'),
    path('connect/', views.connect, name='connect'),
]
