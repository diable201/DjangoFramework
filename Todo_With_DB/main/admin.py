from django.contrib import admin
from .models import Task, TodoList


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ('title',)
    list_display = (
        'title',
        'created',
        'due_on',
        'owner',
        'done'
    )
    search_fields = (
        'title',
        'owner'
    )
    list_filter = ('done',)


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    search_fields = (
        'title',
    )

