from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def HomePage(request):
    return render(request, 'index.html')

def SignupPageAndLogin(request):
    if request.method == 'POST':
        if 'Name1' in request.POST:  # Sign up form
            uname = request.POST.get('Name1')
            email = request.POST.get('Email1')
            pass1 = request.POST.get('Password1')

            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered')
            else:
                user = User.objects.create_user(username=uname, email=email, password=pass1)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect("SignupPageAndLogin")

        elif 'Email2' in request.POST:  # Login form
            email = request.POST.get('Email2')
            pass1 = request.POST.get('Password2')
            user = authenticate(request, username=email, password=pass1)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
               return redirect('index')

    return render(request, 'SignupPageAndLogin.html')

def logout_user(request):
    logout(request)
    return redirect('SignupPageAndLogin')