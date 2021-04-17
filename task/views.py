from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .models import Task
from .forms import *

def list_tasks(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'task/list.html', context)

def task_description(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'task/description.html', {'task':task} )

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.delete()

    return redirect('/')