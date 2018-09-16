from django.urls import path, re_path
from main import views

urlpatterns = [
    path('', views.todo_list, name="todo_list"),
    path('completed', views.completed_todo_list, name="completed_todo_list"),
    re_path(r'^\d+/completed/$', views.completed_todo_list),
]