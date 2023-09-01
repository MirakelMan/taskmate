from django.contrib import admin
import todolist_app.models as todo_models

# Register your models here.
admin.site.register(todo_models.Task)
