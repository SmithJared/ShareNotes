from django.urls import path
from . import views

urlpatterns = [
    # put your paths here
    path("", views.index, name="index")
]