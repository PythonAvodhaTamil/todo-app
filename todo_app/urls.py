from django.urls import path,include
from todo_app import views


urlpatterns = [
    path('',views.add_task,name='add_task'),
    path('task/',views.task,name='task'),
    path('delete/<int:id>',views.delete,name='delete')
    
]



    