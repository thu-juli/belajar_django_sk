from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def loginPage(request):
    if request.method == "POST":
        username_input = request.POST['username']
        password_input = request.POST['password']
        user = authenticate(request, username=username_input,
                            password=password_input)
        if user is not None:
            login(request, user)
            return redirect('home')

    context = {
        'page_title': 'Login Page'
    }

    return render(request, 'login_page.html', context)


@login_required(login_url='login')
def logoutPage(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

    context = {
        'page_title': 'Logout Page'
    }
    return render(request, 'logout_page.html', context)


def home(request):
    context = {
        'page_title': 'HOME'
    }
    return render(request, 'index.html', context)
