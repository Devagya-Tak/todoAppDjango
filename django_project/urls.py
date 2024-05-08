from django.contrib import admin
from django.urls import path
from home.views import todo_list_create, todo_retrieve_update_destroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos/', todo_list_create, name='todo-list-create'),
    path('api/todos/<int:pk>/', todo_retrieve_update_destroy, name='todo-detail'),
]
