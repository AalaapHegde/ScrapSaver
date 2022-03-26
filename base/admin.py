from django.contrib import admin
from .models import Task, UserInfo, Users
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class UserAdminInfo(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['username', 'organizationName', 'password', 'zipCode']}),
    ]

    list_display = ('username', 'organizationName', 'password', 'zipCode')


admin.site.register(UserInfo, UserAdminInfo)
admin.site.register(Task)
admin.site.register(Users, UserAdmin)
