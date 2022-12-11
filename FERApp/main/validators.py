from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _


no_space_pass_validator = RegexValidator(r' ', _('Password must not contain spaces!'),
                                         inverse_match=True, code='invalid_text')

no_space_title_validator = RegexValidator(r' ', _('Title must not contain spaces!'),
                                          inverse_match=True, code='invalid_text')


def validate_file_size(value):
    if value.size > 5 * 1024 * 1024:
        raise ValidationError(_("You cannot upload file with size more than 5Mb"))
    else:
        return value
