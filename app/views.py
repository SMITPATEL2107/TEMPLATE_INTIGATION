from django.shortcuts import render
from random import randint
from .models import *

# Create your views here.

def IndexPage(request):
    return render(request,"app/index.html")



def Register(request):
    uname = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    otp =  randint(10000,99999)
    newuser = User.objects.create(username=uname,email=email,password=password,otp=otp)
    return render(request,"app/login.html")



def Login(request):
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.get(email=email)

    if user:
        if user.password==password:
            request.session['username'] = user.username
            request.session['email'] = user.email

            return render(request,"app/home.html")
    else:
        message = "User doesnot exist"
        return render(request,"app/login.html",{'message':message})