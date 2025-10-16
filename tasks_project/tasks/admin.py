from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Task


admin.site.register(User, UserAdmin)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'priority', 'status', 'due_date', 'completed_at')
    list_filter = ('status', 'priority', 'due_date')
    search_fields = ('title', 'description', 'owner__username')
    ordering = ('-created_at',)
