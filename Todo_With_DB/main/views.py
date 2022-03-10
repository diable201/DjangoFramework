from django.shortcuts import render
from .models import Task


# Create your views here.
def all_todos(request, group_id):
    context = {
        'todos': Task.objects.filter(group_id=group_id).order_by('title'),
    }
    return render(request, 'todos/all_tasks.html', context=context)


def completed_todos(request, group_id):
    context = {
        'todos': Task.objects.filter(group_id=group_id, done=True).order_by('title')
    }
    return render(request, 'todos/completed_tasks.html', context=context)
