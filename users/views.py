from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("success")
            login(request, user)
            return redirect('index')
        else:
            print("Fail")
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect("user:login")  

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            print(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']

            user = User.objects.create_user(username, email, password)
            user.last_name = lastname
            user.first_name = firstname
            user.save()
            return redirect('index')
    return render(request, 'signup.html')