from django.urls import path
from .views import all_todos, completed_todos

urlpatterns = [
    path('todos/', all_todos),
    path('todos/completed/', completed_todos)
]
