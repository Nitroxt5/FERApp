import logging

from django.shortcuts import render, redirect
from django.utils.translation import gettext as _

from .forms import PassForm, ImageForm


def index(request):
    if not request.user.is_authenticated:
        return redirect('auth', permanent=True)
    return render(request, 'main.html', context={'change_form': PassForm(), 'img_form': ImageForm(), 'upload_err': ''})


def image_upload_view(request):
    if not request.user.is_authenticated:
        return redirect('auth', permanent=True)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if not form.is_valid():
            error_msg = next(filter(lambda el: el != [''], form.errors.values()), '')[0]
            logging.debug(f'Form is invalid: {error_msg}')
            return render(request, 'main.html', context={'change_form': PassForm(), 'img_form': ImageForm(),
                                                         'swap': True, 'upload_err': _(error_msg)})
        form.instance.user = request.user
        form.save()
        return render(request, 'main.html', context={'change_form': PassForm(), 'img_form': form,
                                                     'img_obj': form.instance, 'swap': True, 'upload_err': ''})
    return redirect('main', permanent=True)
