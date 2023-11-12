from django.contrib import admin

# Register your models here.

from invoices.models import Invoice, InvoiceHistory

admin.site.register(InvoiceHistory)
admin.site.register(Invoice)
