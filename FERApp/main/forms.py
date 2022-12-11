from django import forms
from django.utils.translation import gettext as _

from .models import Image
from .validators import no_space_pass_validator


class PassForm(forms.Form):
    old_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,
                                   validators=[no_space_pass_validator],
                                   error_messages={'required': _('Password field is required'),
                                                   'min_length': _('Ensure password has at least 8 characters'),
                                                   'max_length': _('Ensure password has less than 20 characters')})
    new_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,
                                   validators=[no_space_pass_validator],
                                   error_messages={'required': _('Password field is required'),
                                                   'min_length': _('Ensure password has at least 8 characters'),
                                                   'max_length': _('Ensure password has less than 20 characters')})


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('user', 'title', 'image')
