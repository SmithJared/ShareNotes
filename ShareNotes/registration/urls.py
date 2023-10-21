from django.urls import path
from . import views

urlpatterns = [
    # put your paths here
    path("registration/", views.registration, name="registration"),
    path("login/", views.login, name="login"),
]