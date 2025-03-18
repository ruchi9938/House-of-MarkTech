from django.urls import path
from .views import user_login, user_logout, dashboard, task_list, task_create, task_detail, update_task

urlpatterns = [
     path('', task_list, name='task_list'),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", user_logout, name="logout"),
    path("tasks/", task_list, name="task-list"),
    path("tasks/create/", task_create, name="task-create"),
    path('task/<int:task_id>/', task_detail, name='task_detail'),
    path("task/<int:task_id>/update/", update_task, name="update_task"),
]
