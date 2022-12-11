from django.core.validators import RegexValidator
from django.utils.translation import gettext as _


no_space_validator = RegexValidator(r' ', _('Username and password must not contain spaces!'),
                                    inverse_match=True, code='invalid_text')
