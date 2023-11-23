import logging
from django.core.mail import mail_admins
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseServerError


class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            # Log the exception
            logging.exception(str(e))
            # Send Emails to the site administrators
            subject = f"{_('Exception occurred:')} {request.path}"
            message = f"{_('Exception occurred while processing')} {request.path}:\n{str(e)}"
            mail_admins(subject, message)
            # Return a custom error page
            response = HttpResponseServerError(f"{_('Oops! Something went wrong.')}")
        return response