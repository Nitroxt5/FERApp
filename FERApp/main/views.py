import logging

from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.http import FileResponse

from .forms import PassForm, ImageForm
from .img_handler import evaluate_emotions


def index(request):
    if not request.user.is_authenticated:
        return redirect('auth', permanent=True)
    return render(request, 'main.html', context={'change_form': PassForm(), 'img_form': ImageForm(), 'upload_err': ''})


def image_upload_recognize(request):
    if not request.user.is_authenticated:
        return redirect('auth', permanent=True)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if not form.is_valid():
            error_msg = next(filter(lambda el: el != [''], form.errors.values()), '')[0]
            logging.info(f'Form is invalid: {error_msg}')
            return render(request, 'main.html', context={'change_form': PassForm(), 'img_form': ImageForm(),
                                                         'swap': True, 'upload_err': _(error_msg)})
        form.instance.user = request.user
        form.save()
        evaluate_emotions(form.instance)
        request.user.profile.uploads_count += 1
        request.user.profile.save()
        return render(request, 'main.html', context={'change_form': PassForm(), 'img_form': form,
                                                     'img_obj': form.instance, 'swap': True, 'upload_err': ''})
    return redirect('main', permanent=True)


def image_download(request):
    return redirect('main', permanent=True)
