from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from accounts.models import CustomUser


def post_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user:
            if user.type == 'E':
                login(request, user)
                return redirect('/vacancy/')
            elif user.type == 'C':
                login(request, user)
                return redirect('/candidate/')
        else:
            print('User is not authenticated')
    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        user = CustomUser(
            username=request.POST.get('username'),
            first_name=request.POST.get('first'),
            last_name=request.POST.get('last'),
            type=request.POST.get('role'),
        )
        user.set_password(password)
        user.save()
        return redirect('/login')

    return render(request, 'registration.html')
