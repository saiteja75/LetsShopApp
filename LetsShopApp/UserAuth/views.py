from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def forgot(request):
    return render(request, "forgot.html")
