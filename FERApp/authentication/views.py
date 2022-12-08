import logging
from .forms import LogForm, RegForm

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


def index(request):
    return render(request, 'base_auth.html', context={'signup': False, 'log_err': '', 'reg_err': '',
                                                      'log_form': LogForm(), 'reg_form': RegForm()})


def log_in(request):
    if request.user.is_authenticated:
        return redirect("main", permanent=True)
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['log_username'], password=request.POST['log_password'])
            if user is not None:
                login(request, user)
                return redirect('main', permanent=True)
    return render(request, 'base_auth.html',
                  context={'signup': False, 'log_err': _('Wrong username or password!'),
                           'reg_err': '', 'log_form': LogForm(), 'reg_form': RegForm()})


def log_out(request):
    logout(request)
    return redirect('auth', permanent=True)


def register(request):
    if request.user.is_authenticated:
        return redirect("main", permanent=True)
    if request.method == 'POST':
        form = RegForm(request.POST)
        if not form.is_valid():
            error_msg = next(filter(lambda el: el != [''], form.errors.values()), '')[0]
            return render(request, 'base_auth.html',
                          context={'signup': True, 'log_err': '', 'reg_err': error_msg,
                                   'log_form': LogForm(), 'reg_form': RegForm()})
        try:
            user = User.objects.create_user(request.POST['reg_username'], '', request.POST['reg_password'])
        except IntegrityError:
            return render(request, 'base_auth.html',
                          context={'signup': True, 'log_err': '', 'reg_err': _('Username already exists!'),
                                   'log_form': LogForm(), 'reg_form': RegForm()})
        user.save()
        login(request, user)
    return redirect('main', permanent=True)
