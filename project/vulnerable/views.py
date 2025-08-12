from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# demo home shows "visit this project" link; C2 will flip a variable to simulate DNS hijack

def demo_home(request):
    # normal demo page
    return render(request, 'vulnerable/demo_home.html')


def demo_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'vulnerable/login.html')