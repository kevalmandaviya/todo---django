from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

def addTask(request):
    if request.method == "POST":
        task = request.POST.get('task')
        Task.objects.create(title=task)
    return redirect('home')

def mark_as_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, task_id):
    get_task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        new_title = request.POST.get('task')
        get_task.title = new_title
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task
        }
    return render(request, 'edit_task.html', context)

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')
