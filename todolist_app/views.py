from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from typing import MutableMapping, Self
import todolist_app.models as todo_models
import todolist_app.forms as todo_forms
from django.contrib.auth.decorators import login_required


class Context(dict):
    _base = {"app_name": "MirakelTasks"}

    def __init__(self, _dict: MutableMapping[str, str]) -> Self:
        _dict.update(self._base)
        super().__init__(_dict)


@login_required
def todolist(request: HttpRequest):
    if request.method == "POST":
        print(request.POST)
        form = todo_forms.TaskForm(request.POST or None)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.owner = request.user
            form_instance.save()
        messages.success(request, "New task succesfully saved.")
        return redirect("todolist")
    else:
        tasks = todo_models.Task.objects.filter(owner=request.user)
        paginator = Paginator(tasks, 10)
        page = request.GET.get("page")
        display_tasks = paginator.get_page(page)
        context = Context(
            {
                "title": "To-Do List",
                "first_arg": "Pascal",
                "tasks": display_tasks,
            }
        )
        return render(request=request, template_name="todolist.html", context=context)


@login_required
def delete_task_from_todo_list(request: HttpRequest, task_id: int):
    task = todo_models.Task.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else:
        messages.error(request, "You are not authorized to delete that task.")
    return redirect("todolist")


@login_required
def update_task_from_todo_list(request: HttpRequest, task_id: int):
    if request.method == "POST":
        task = todo_models.Task.objects.get(pk=task_id)
        form = todo_forms.TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, "Task succesfully updated.")
        return redirect("todolist")
    else:
        task = todo_models.Task.objects.get(pk=task_id)
        context = Context(
            {
                "title": "Update Task",
                "task": task,
            }
        )
        return render(
            request=request, template_name="update_task.html", context=context
        )


@login_required
def toggle_done_task_from_todo_list(request: HttpRequest, task_id: int):
    task = todo_models.Task.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = not task.done
        task.save()
    else:
        messages.error(
            request, "Unauthorized request. You can't update status of that task."
        )
    return redirect("todolist")


def contact(request):
    context = Context(
        {
            "title": "Contact Us",
            "first_arg": "Helena",
        }
    )
    return render(request=request, template_name="contact.html", context=context)


def about(request):
    context = Context(
        {
            "title": "About Us",
            "first_arg": "Telma",
        }
    )
    return render(request=request, template_name="about.html", context=context)


def index(request):
    context = Context(
        {
            "title": "HomePage",
            "first_arg": "Matthias",
        }
    )
    return render(request=request, template_name="index.html", context=context)
