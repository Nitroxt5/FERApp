from django import forms
from django.core.validators import RegexValidator


_no_space_validator = RegexValidator(r' ', 'Username and password must not contain spaces!',
                                     inverse_match=True, code='invalid_text')


class LogForm(forms.Form):
    log_username = forms.CharField(min_length=5, max_length=15, widget=forms.TextInput(attrs={'autocomplete': 'off'}),
                                   validators=[_no_space_validator])
    log_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,
                                   validators=[_no_space_validator])


class RegForm(forms.Form):
    reg_username = forms.CharField(min_length=5, max_length=15, widget=forms.TextInput(attrs={'autocomplete': 'off'}),
                                   validators=[_no_space_validator])
    reg_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,
                                   validators=[_no_space_validator])
    reg_confirm_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,
                                           validators=[_no_space_validator])
