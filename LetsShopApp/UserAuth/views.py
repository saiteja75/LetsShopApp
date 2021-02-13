from django.shortcuts import render, redirect
from UserAuth import logic as lg
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "home.html")

def login(request):
    if request.method == "POST":
        user = lg.authenticateUser(request)
        print(user)
        if user is not None:
            messages.success(request, "Login Successful")
            return render(request, 'home.html')
        else:
            messages.warning(request, "Login Failed")
    return render(request, "login.html")

def signup(request):
    if request.method == "POST":
        status = lg.registerTheUser(request)
        print(status)
        if(status):
            messages.success(request, "User Registered Successfully")
            return render(request, 'login.html')
        else:
            messages.warning(request, "Not Registered")
    return render(request, "signup.html")

def forgot(request):
    return render(request, "forgot.html")

def logout(request):
    lg.logoutUser(request)
    return render(request, "home.html")
