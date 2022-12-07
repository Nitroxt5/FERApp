from django.contrib.auth import authenticate
from django.shortcuts import render


def index(request):
    return render(request, 'auth.html')


def login(request):
    return render(request, 'auth.html')


def register(request):
    authenticate()
    return render(request, 'auth.html')
