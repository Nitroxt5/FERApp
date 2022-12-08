from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

_no_space_validator = RegexValidator(r' ', _('Username and password must not contain spaces!'),
                                     inverse_match=True, code='invalid_text')


class LogForm(forms.Form):
    log_username = forms.CharField(min_length=5, max_length=15, widget=forms.TextInput(attrs={'autocomplete': 'off'}),
                                   validators=[_no_space_validator], error_messages={'required': _('Login field is required')})
    log_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,
                                   validators=[_no_space_validator], error_messages={'required': _('Password field is required')})


class RegForm(forms.Form):
    reg_username = forms.CharField(min_length=5, max_length=15, widget=forms.TextInput(attrs={'autocomplete': 'off'}),
                                   validators=[_no_space_validator], error_messages={'required': _('Login field is required')})
    reg_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,
                                   validators=[_no_space_validator], error_messages={'required': _('Password field is required')})
    reg_confirm_password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,
                                           validators=[_no_space_validator], error_messages={'required': _('Password field is required')})

    def clean_reg_confirm_password(self):
        cd = self.cleaned_data
        if cd['reg_password'] != cd['reg_confirm_password']:
            raise forms.ValidationError(_('Passwords do not match.'), code='pass_not_match')
        return cd['reg_confirm_password']
