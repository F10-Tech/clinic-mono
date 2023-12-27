from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (None, {
        'classes': ('wide',),
        'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'phone', 'otp'),
    }),

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'membership', 'first_name', 'last_name')
    list_filter = ('membership',)
    list_editable = ('membership',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    ordering = ('-user__first_name', '-user__last_name')
