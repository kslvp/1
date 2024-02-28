from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

def login_view(request):
    # Your login view logic here
    return HttpResponse("Login Page")

def logout_view(request):
    # Your logout view logic here
    return HttpResponse("Logout Page")




