from django.contrib import admin
from .models import Ingredient, UserInfo, Users
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['username', 'email', 'first_name', 'last_name', 'is_staff']}),
    ]

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')


admin.site.register(Ingredient)
admin.site.register(Users, CustomUserAdmin)
