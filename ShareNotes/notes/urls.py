from django.contrib import admin  
from django.urls import path
from . import views

urlpatterns = [
    # put your paths here
    path('admin/', admin.site.urls),  
    path('index/', views.index),  
    path("", views.index, name="index")
]

