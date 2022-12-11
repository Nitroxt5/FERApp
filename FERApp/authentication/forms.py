from django import forms
from django.utils.translation import gettext as _

from .validators import no_space_validator


class LogForm(forms.Form):
    log_username = forms.CharField(min_length=5, max_length=15, widget=forms.TextInput(attrs={'autocomplete': 'off'}),
                                   validators=[no_space_validator],
                                   error_messages={'required': _('Username field is required'),
                                                   'min_length': _('Ensure username has at least 5 characters'),
                                                   'max_length': _('Ensure username has less than 15 characters')})
    log_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,
                                   validators=[no_space_validator],
                                   error_messages={'required': _('Password field is required'),
                                                   'min_length': _('Ensure password has at least 8 characters'),
                                                   'max_length': _('Ensure password has less than 20 characters')})


class RegForm(forms.Form):
    reg_username = forms.CharField(min_length=5, max_length=15, widget=forms.TextInput(attrs={'autocomplete': 'off'}),
                                   validators=[no_space_validator],
                                   error_messages={'required': _('Username field is required'),
                                                   'min_length': _('Ensure username has at least 5 characters'),
                                                   'max_length': _('Ensure username has less than 15 characters')})
    reg_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,
                                   validators=[no_space_validator],
                                   error_messages={'required': _('Password field is required'),
                                                   'min_length': _('Ensure password has at least 8 characters'),
                                                   'max_length': _('Ensure password has less than 20 characters')})
    reg_confirm_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,
                                           validators=[no_space_validator],
                                           error_messages={'required': _('Password field is required'),
                                                           'min_length': _('Ensure password has at least 8 characters'),
                                                           'max_length': _('Ensure password has less than 20 characters')})

    def clean_reg_confirm_password(self):
        cd = self.cleaned_data
        if cd['reg_password'] != cd['reg_confirm_password']:
            raise forms.ValidationError(_('Passwords do not match.'), code='pass_not_match')
        return cd['reg_confirm_password']


class PassForm(forms.Form):
    old_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,
                                   validators=[no_space_validator],
                                   error_messages={'required': _('Password field is required'),
                                                   'min_length': _('Ensure password has at least 8 characters'),
                                                   'max_length': _('Ensure password has less than 20 characters')})
    new_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,
                                   validators=[no_space_validator],
                                   error_messages={'required': _('Password field is required'),
                                                   'min_length': _('Ensure password has at least 8 characters'),
                                                   'max_length': _('Ensure password has less than 20 characters')})
