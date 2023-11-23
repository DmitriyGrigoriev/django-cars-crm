import os

# https://django-environ.readthedocs.io/en/latest/tips.html#email-settings
# DJANGO_ADMINS=Blake:blake@cyb.org,Alice:alice@cyb.org
ADMINS = [x.split(':') for x in os.getenv('DJANGO_ADMINS').split(',')]
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', default='mx1.ntbroker.ru')
SERVER_EMAIL = os.getenv('SERVER_EMAIL', default='exchange@ntbroker.ru')
EMAIL_HOST_USER = os.getenv('SG_USER', default='exchange')
EMAIL_HOST_PASSWORD = os.getenv('SG_PWD', default=None)
EMAIL_SUBJECT_PREFIX = os.getenv('EMAIL_SUBJECT_PREFIX')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_USE_TLS = False
EMAIL_PORT = 25
