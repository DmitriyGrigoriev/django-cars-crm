from django.utils.translation import gettext_lazy as _


class Messages(object):
    REQUARED_PARAMETER_MISSING = _('Отсутствует обязательный параметр: {0}')
    INVALID_VALUE_PARAMETER = _('Недопустимое значение: {0}')
    SMTP_ERROR = _('Error was occurred due to sent email: {0}')
