from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.contrib.staticfiles import *

def cooplog(request):
    print request
    if request.method == "POST":
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

    if request.method == "GET":
        return render(request, 'login.html')
       
    else:
        return HttpResponse("There seems to be a problem!")