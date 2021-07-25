from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomChangeForm
    model = CustomUser
    list_display = ("email", "username", "age", "is_staff")
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': {'age', }
        }),
    )
    fieldsets = UserAdmin.fieldsets + (
     (None, {
            'fields': {'age', }
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
