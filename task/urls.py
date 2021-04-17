from django.urls import path
from .views import list_tasks, task_description, delete_task

app_name = 'tasks'

urlpatterns = [
    path('', list_tasks, name='list'),
    path('<int:task_id>/description/', task_description, name='description'),
    path('<int:task_id>/delete/', delete_task, name='delete')
]
