from django.urls import path, re_path
from main import views

urlpatterns = [
    path('', views.todo_list, name="todo_list"),
    path('completed', views.completed_todo_list, name="completed_todo_list"),
    # re_path(r'^\d+/completed/$', views.completed_todo_list),
    # re_path(r'^\d+/completed/$', views.completed_todo_list),
    path('add', views.todo_add, name="todo_add"),
    path('completed', views.completed_todo_list, name="completed_todo_list"),
    path('delete_complete_list', views.delete_complete_list, name="delete_complete_list"),
    path('delete_incomplete_list', views.delete_incomplete_list, name="delete_incomplete_list"),
    path('delete/<int:todo_id>', views.todo_delete, name='todo_delete'),
]