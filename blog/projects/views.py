from django.shortcuts import render
from projects.models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def index(request):
    return render(request,'index.html')

def aboutme(request):
    return render(request, 'aboutme.html')

def about(request):
    return render(request, 'about.html')

def credits(request):
    return render(request, 'credits.html')