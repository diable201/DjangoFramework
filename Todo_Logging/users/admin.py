from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'username',
        'first_name',
        'last_name'
    )
    search_fields = (
        'email',
        'username'
    )
    list_filter = (
        'is_active',
    )
