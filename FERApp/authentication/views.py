import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from .forms import LogForm, RegForm, PassForm


def index(request):
    if request.user.is_authenticated:
        return redirect('main', permanent=True)
    return render(request, 'base_auth.html', context={'swap': False, 'log_err': '', 'reg_err': '',
                                                      'log_form': LogForm(), 'reg_form': RegForm()})


def log_in(request):
    if request.user.is_authenticated:
        return redirect('main', permanent=True)
    if request.method == 'POST':
        form = LogForm(request.POST)
        if not form.is_valid():
            error_msg = next(filter(lambda el: el != [''], form.errors.values()), '')[0]
            logging.debug(f'Form is invalid: {error_msg}')
            return render(request, 'base_auth.html', context={'swap': False, 'log_err': _(error_msg), 'reg_err': '',
                                                              'log_form': LogForm(), 'reg_form': RegForm()})
        user = authenticate(username=request.POST['log_username'], password=request.POST['log_password'])
        if user is not None:
            login(request, user)
            return redirect('main', permanent=True)
        return render(request, 'base_auth.html', context={'swap': False, 'log_err': _('Wrong username or password!'),
                                                          'reg_err': '', 'log_form': LogForm(), 'reg_form': RegForm()})
    return redirect('auth', permanent=True)


def log_out(request):
    logout(request)
    return redirect('auth', permanent=True)


def register(request):
    if request.user.is_authenticated:
        return redirect('main', permanent=True)
    if request.method == 'POST':
        form = RegForm(request.POST)
        if not form.is_valid():
            error_msg = next(filter(lambda el: el != [''], form.errors.values()), '')[0]
            logging.info(f'Form is invalid: {error_msg}')
            return render(request, 'base_auth.html', context={'swap': True, 'log_err': '', 'reg_err': _(error_msg),
                                                              'log_form': LogForm(), 'reg_form': RegForm()})
        try:
            user = User.objects.create_user(request.POST['reg_username'], '', request.POST['reg_password'])
        except IntegrityError:
            return render(request, 'base_auth.html', context={'swap': True, 'log_err': '', 'reg_err': _('Username already exists!'),
                                                              'log_form': LogForm(), 'reg_form': RegForm()})
        user.save()
        login(request, user)
        return redirect('main', permanent=True)
    return redirect('auth', permanent=True)


def change_pass(request):
    if not request.user.is_authenticated:
        return redirect('auth', permanent=True)
    if request.method == 'POST':
        form = PassForm(request.POST)
        if not form.is_valid():
            error_msg = next(filter(lambda el: el != [''], form.errors.values()), '')[0]
            logging.info(f'Form is invalid: {error_msg}')
            messages.error(request, _(error_msg))
            return redirect('main', permanent=True)
        user = authenticate(username=request.user.username, password=request.POST['old_password'])
        if user is not None:
            user.set_password(request.POST['new_password'])
            user.save()
            login(request, user)
            messages.success(request, _('Password successfully changed!'))
            return redirect('main', permanent=True)
        messages.error(request, _('Old password is wrong!'))
    return redirect('main', permanent=True)
