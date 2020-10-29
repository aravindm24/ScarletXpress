from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    return render(request, 'myR/home.html')
