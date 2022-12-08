from django.shortcuts import render, redirect

from .forms import PassForm


def index(request):
    if not request.user.is_authenticated:
        return redirect('auth', permanent=True)
    return render(request, 'main.html', context={'form': PassForm()})
