from django.urls import path
from .views import all_todos

urlpatterns = [
    path('', all_todos)
]
