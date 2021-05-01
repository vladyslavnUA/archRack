from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'name', 'last_login', 'updated_at', 'created_at', 'is_staff', 'is_active',]
    # [field.name for field in CustomUser._meta.concrete_fields]
    # ('name', 'email', 'is_staff', 'is_active',)
    list_filter = ('name', 'email', 'created_at', 'updated_at', 'is_staff', 'is_active',)
    readonly_fields = ['created_at', 'updated_at',]
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'date_joined', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)