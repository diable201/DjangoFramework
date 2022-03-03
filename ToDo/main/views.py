import datetime
from django.shortcuts import render

todos = [
    {
        'task': 'Task 1',
        'created': datetime.datetime.today().strftime("%d/%m/%y"),
        'due_on': "10/09/2022",
        'owner': 'admin',
        'done': True
    },
    {
        'task': 'Task 3',
        'created': datetime.datetime.today().strftime("%d/%m/%y"),
        'due_on': "02/07/2022",
        'owner': 'akuma',
        'done': True
    }
]

done_todos = [
    {
        'task': 'Task 0',
        'created': datetime.datetime.today().strftime("%d/%m/%y"),
        'due_on': "10/09/2022",
        'owner': 'admin',
        'done': False
    },
    {
        'task': 'Task 2',
        'created': datetime.datetime.today().strftime("%d/%m/%y"),
        'due_on': "07/09/2022",
        'owner': 'admin',
        'done': True
    },
]


# Create your views here.
def all_todos(request):
    context = {
        'todos': todos
    }
    return render(request, 'todos/all_tasks.html', context=context)


def completed_todos(request):
    context = {
        'todos': done_todos
    }
    return render(request, 'todos/completed_tasks.html', context=context)
