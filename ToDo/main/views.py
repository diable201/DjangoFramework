import datetime
from django.shortcuts import render


# Create your views here.
def all_todos(request):
    todos = [
        {
            'task': 'Task 2',
            'created': datetime.datetime.now(),
            'due_on': datetime.datetime.now() + datetime.timedelta(days=2),
            'owner': 'admin',
            'done': True
        },
        {
            'task': 'Task 3',
            'created': datetime.datetime.now(),
            'due_on': datetime.datetime.now() + datetime.timedelta(days=2),
            'owner': 'admin',
            'done': True
        },
        {
            'task': 'Task 4',
            'created': datetime.datetime.now(),
            'due_on': datetime.datetime.now() + datetime.timedelta(days=2),
            'owner': 'admin',
            'done': True
        }
    ]
    context = {
        'todos': todos
    }
    return render(request, 'todos.html', context=context)
