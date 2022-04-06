from django.contrib import admin
from .models import Task, TodoList


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ('title',)
    list_display = (
        'id',
        'owner',
        'group',
        'title',
        'created_at',
        'due_date',
        'status'
    )
    search_fields = (
        'title',
        'owner__username',
        'group__title'
    )
    list_editable = ('status',)
    list_filter = ('status', 'group', 'owner')


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    class TaskInline(admin.TabularInline):
        model = Task
        extra = 1
    list_display = (
        'id',
        'title',
    )
    search_fields = (
        'title',
    )
    inlines = (TaskInline,)
