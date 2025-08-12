from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def base(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'home.html')


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome {username}!")
            return redirect('home')  # Redirect to user's dashboard/projects
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')  # Re-render home with modal

    return redirect('home')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('home')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('home')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created! You can log in now.")
        return redirect('home')

    return redirect('home')


def signout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')

def index(request):
    return render(request, 'portfolio/index.html')


def projects(request):
    # show links to subdomain demos
    return render(request, 'portfolio/projects.html')

def contact(request):
    return render(request, 'portfolio/contact.html')