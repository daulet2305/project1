from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.get_todos),
    path('todos/<int:id>/', views.get_todo_by_id),
    path('todos/create/', views.create_todo),
    path('todos/<int:id>/delete/', views.delete_todo),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),  
    path('create/', views.create_todo_view, name='create_todo'),  
    path('<int:id>/delete/', views.delete_todo_view, name='delete_todo'),  
]