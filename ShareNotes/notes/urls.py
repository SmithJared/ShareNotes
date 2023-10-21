from django.contrib import admin  
from django.urls import path
from . import views

urlpatterns = [
    # put your paths here
    path('admin/', admin.site.urls),  
    path('upload/', views.upload, name='upload'),
    path('student/<str:last_name>/', views.student, name="student"),
    path('create_note/<int:recipient_id>/', views.create_note, name='create_note'),
    path('inbox/', views.inbox, name='inbox'),
    path('select-classroom/', views.select_classroom, name='select_classroom'),
    path('classroom/', views.classroom, name='classroom'),
]

