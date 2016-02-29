from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.contrib.staticfiles import *

def cooplog(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("Successfully Logged In")
        else:
            return HttpResponse("Locked Out")   
    else:
        return HttpResponse("Invalid Credentials")

def cooplogin(request):
    return render(request, 'login.html')
       
