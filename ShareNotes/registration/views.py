from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def registration(req:HttpRequest):
    if req.method == "POST":
        user = User.objects.create_user(
            username=req.POST.get("email"),
            password=req.POST.get("psw"),
            email=req.POST.get("email"),
            first_name=req.POST.get("first_name"),
            last_name=req.POST.get("last_name")
        )
        login(req,user)
        return render(req,"/notes/index/")
    else:
        return render(req, "registration/registration.html", {"url": "/registration/"})


def log_in(req:HttpRequest):
    logout(req)
    if req.method == "POST":
        user = authenticate(req, username=req.POST.get("email"), password=req.POST.get("psw"))
        print(req.POST.get("psw"))
        if user is not None:
            login(req, user) # this is the part I missed
            return render(req,"/notes/index/")
        
        return render(req, "registration/login.html", {"url": "/login/"})
    else:
        return render(req, "registration/login.html", {"url": "/login/"})


def log_out(req):
    logout(req)
    return redirect("/")