from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def registration(req:HttpRequest):
    if req.method == "POST":
        user = User.objects.create_user(
            username=req.POST.get("email"),
            password=req.POST.get("password"),
            email=req.POST.get("email"),
            first_name=req.POST.get("first_name"),
            last_name=req.POST.get("last_name")
        )
        login(req,user)
        return HttpResponse("<h1>You are Registered</h1>")
    else:
        return render(req, "registration/registration.html")


def log_in(req:HttpRequest):
    if req.method == "POST":
        user = authenticate(req, username=req.POST.get("email"), password=req.POST.get("password"))
        if user is not None:
            login(req, user) # this is the part I missed
            return HttpResponse("<h1>You are Logged In<h1>")
        
        return redirect("/registration/")
    else:
        return redirect("/registration/")


def logout(req):
    logout(req)
    return redirect("/")