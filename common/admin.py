from django.contrib import admin
from common.models import User, Address, Comment, Comment_Files, Company

# Register your models here.

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Comment)
admin.site.register(Company)
admin.site.register(Comment_Files)
