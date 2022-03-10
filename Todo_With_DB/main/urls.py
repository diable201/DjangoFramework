from django.urls import path
from .views import all_todos, completed_todos

urlpatterns = [
    path('todos/<int:group_id>/', all_todos),
    path('todos/<int:group_id>/completed/', completed_todos)
]
