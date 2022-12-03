from django.contrib.auth import login, authenticate
from django.shortcuts import render, HttpResponse, redirect
from src.user.forms import CustomUserCreationForm, CustomUserLoginForm


def registration(request, *args, **kwargs):
    if request.user.is_authenticated:
        return HttpResponse(f"Você já está logado, mané")
    context = {}
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            authenticate(email=request.POST.get('email'), password=request.POST.get('password1'))
            login(request, user)
            return redirect("product:home")
        else:
            context['registration_form'] = form
    return render(request, 'user/registration.html', context=context)


def login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return HttpResponse(f"Você já está logado, mané")
    context = {}
    if request.POST:
        form = CustomUserLoginForm(request.POST)
        user = authenticate(email=request.POST.get('email'),password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect("product:home")
        else:
            context['login_form'] = form
    return render(request, 'user/login.html', context=context)
    