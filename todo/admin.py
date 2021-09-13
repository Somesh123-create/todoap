from django.contrib import admin
from .models import Task, Category
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'description', 'task_date', 'completed')


admin.site.register(Task, TaskAdmin)
admin.site.register(Category)
