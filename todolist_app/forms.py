from django import forms
import todolist_app.models as todo_models


class TaskForm(forms.ModelForm):
    class Meta:
        model = todo_models.Task
        fields = ["task", "done"]
