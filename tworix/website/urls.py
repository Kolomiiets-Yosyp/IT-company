from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('solutions/', views.solutions, name='solutions'),
    path('rules/', views.rules, name='rules'),
    path('lab/', views.lab, name='lab'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('connect/', views.connect, name='connect'),
    path('build/', views.BuildView.as_view(), name='build'),
    path('grid/', views.GridView.as_view(), name='grid'),
    path('core/', views.CoreView.as_view(), name='core'),
    path('directory/', views.DirectoryView.as_view(), name='directory'),
    path('the_vault/', views.TheVaultView.as_view(), name='the_vault'),
    path('nodes/', views.NodesView.as_view(), name='nodes'),
    path('contact_submit/', views.contact_submit, name='contact_submit'),
]
