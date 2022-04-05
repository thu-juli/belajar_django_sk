from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def index(request):
    listProject = Project.objects.all()
    context = {
        'listproject': listProject,

    }
    return render(request, 'blogs/index.html', context)


def blogs(request, pk):
    projectObj = Project.objects.get(id=pk)

    context = {
        'project': projectObj,
    }
    return render(request, 'blogs/blogs.html', context)


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'blogs/create-project.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid:
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'blogs/create-project.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('index')

    context = {
        'project': project
    }

    return render(request, 'blogs/delete-project.html', context)
