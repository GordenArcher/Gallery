from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib import messages



# Create your views here.
def home(request):
    
    return render(request, 'index.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'signin.html')
            
            
def signout(request):
    logout(request)
    return redirect('home')








