from django.contrib import admin

from common.models import Address, Comment, Comment_Files, User, Org, Profile

# Register your models here.

admin.site.register(Org)
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Comment_Files)
