from django.urls import path
from .views import TodoListViewSet, TodoRetrieveViewSet

urlpatterns = [
    path(
        'todos/<int:group_id>/',
        view=TodoListViewSet.as_view(
             {
                 'get': 'list',
             }
        ),
    ),
    path(
        'todos/',
        view=TodoListViewSet.as_view(
             {
                 'get': 'list',
             }
        ),
    ),
    path(
        'todos/<int:group_id>/<int:pk>/',
        view=TodoListViewSet.as_view(
             {
                 'get': 'retrieve',
             }
        ),
    ),
    path(
        'todos/<int:group_id>/completed/',
        view=TodoRetrieveViewSet.as_view(
             {
                 'get': 'completed',
             }
        ),
    ),
]
