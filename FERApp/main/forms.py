from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

_no_space_validator = RegexValidator(r' ', _('Username and password must not contain spaces!'),
                                     inverse_match=True, code='invalid_text')


class PassForm(forms.Form):
    old_password = forms.CharField(min_length=5, max_length=15, widget=forms.PasswordInput,
                                   validators=[_no_space_validator], error_messages={'required': _('Password field is required')})
    new_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,
                                   validators=[_no_space_validator], error_messages={'required': _('Password field is required')})
