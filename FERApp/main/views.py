import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _

from .forms import PassForm, ImageForm
from .img_handler import evaluate_emotions


@login_required
def index(request):
    return render(request, 'main.html', context={'change_form': PassForm(), 'img_form': ImageForm(), 'upload_err': '',
                                                 'last_img': request.user.profile.last_image})


@login_required
def image_upload_recognize(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if not form.is_valid():
            error_msg = next(filter(lambda el: el != [''], form.errors.values()), '')[0]
            logging.info(f'Form is invalid: {error_msg}')
            return render(request, 'main.html', context={'change_form': PassForm(), 'img_form': ImageForm(),
                                                         'swap': True, 'upload_err': _(error_msg),
                                                         'last_img': request.user.profile.last_image})
        form.instance.user = request.user
        form.save()
        request.user.profile.uploads_count += evaluate_emotions(form.instance)
        request.user.profile.last_image = form.instance.image
        request.user.profile.save()
        return render(request, 'main.html', context={'change_form': PassForm(), 'img_form': form, 'last_img': form.instance.image,
                                                     'rec_img': form.instance.image, 'swap': True, 'upload_err': ''})
    return redirect('main', permanent=True)
