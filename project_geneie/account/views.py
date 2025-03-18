from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

from .models import User


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        print(email, password)  # useful for debugging
        
        if email and password:

            user = authenticate(request, username=email, password=password) 
            print(password) # Authenticate by email
            print(user)
            if user is not None:
                print("You logged in successfully")
                auth_login(request, user)
                return redirect('/')  # Redirect to home page after successful login

            print("Authentication failed")

    return render(request, 'account/login.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if name and email and password1 and password2:
            user = User.objects.create_user(name, email, password1)

            print('User created:', user)
            print(password1)
            return redirect('/login/')
        else:
            print('Somethign went wrong')
    else:
        print('Just show the form!')

    return render(request, 'account/signup.html')