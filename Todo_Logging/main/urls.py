from django.urls import path
from .views import TodoRetrieveViewSet, TodoListViewSet

urlpatterns = [
    # path(
    #     'todos/<int:group_id>/',
    #     view=TodoListViewSet.as_view(
    #         {
    #             'get': 'list',
    #         }
    #     ),
    # ),
    path(
        'todo_lists/',
        view=TodoListViewSet.as_view(
            {
                'get': 'list',
                'post': 'create'
            }
        ),
    ),
    path(
        'todo_lists/<int:pk>/',
        view=TodoListViewSet.as_view(
            {
                'get': 'retrieve',
                'put': 'update'
            }
        ),
    ),
    path(
        'todos/',
        view=TodoRetrieveViewSet.as_view(
            {
                'get': 'list',
                'post': 'create'
            }
        ),
    ),
    path(
        'todos/<int:pk>/',
        view=TodoRetrieveViewSet.as_view(
            {
                'get': 'retrieve',
                'put': 'update'
            }
        ),
    ),
    path(
        'todos/<int:group_id>/todos/',
        view=TodoListViewSet.as_view(
            {
                'get': 'todos',
            }
        ),
    ),
]
