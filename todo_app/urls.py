from django.urls import path,include
from todo_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.add_task,name='add_task'),
    path('task/',views.task,name='task'),
    path('delete/<int:id>',views.delete,name='delete')
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



    