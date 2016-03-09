from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.contrib.staticfiles import *

def cooplog(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'logsuc.html', {'name': user.first_name})
            else:   
                return HttpResponse("Locked Out")   
        else:
            return HttpResponse("Invalid Credentials")

    if request.method == "GET":
        return render(request, 'login.html')
       
    else:
        return HttpResponse("There seems to be a problem!")

def test(request):
    r=request
    print r
    return render(request,r)

def cooplogsuc(request):
    
    return render(request, 'logsuc.html') 

def homepage(request):
    return render(request, 'index.html')            