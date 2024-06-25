from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('', views.FormNameCreateView, name='name_create'),
    path('todo_list/', views.TodoListView, name='todo_list'),
    path('edit_todo/<int:pk>', views.update_todo.as_view(), name="update_todo"),
    path('delete_todo/<int:pk>', views.delete_todo.as_view(), name="delete_todo"),
    path('complete_todo/<int:pk>', views.complete_todo , name="complete_todo")
]
