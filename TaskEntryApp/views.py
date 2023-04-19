from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
# Create your views here.
def HomePage(request):
    return render (request,'home.html')
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        password=request.POST.get('pass')
        confirmpassword=request.POST.get('confirmpass')

        if password!=confirmpassword:
            return HttpResponse("Password and confirm password not equal")    
        else:
            my_user=User.objects.create_user(uname,password,confirmpassword)
            my_user.save()
            return redirect('login')

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")    

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')