from todolist_app import views
from django.urls import path

urlpatterns = [
    path("", views.todolist, name="todolist"),
    path(
        "delete/<task_id>",
        views.delete_task_from_todo_list,
        name="delete_task_from_todo_list",
    ),
    path(
        "update/<task_id>",
        views.update_task_from_todo_list,
        name="update_task_from_todo_list",
    ),
    path(
        "toggle_done/<task_id>",
        views.toggle_done_task_from_todo_list,
        name="toggle_done_task_from_todo_list",
    ),
]
