from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import AppUser


class UserAdmin(BaseUserAdmin):
    # Forms for adding and changing users
    form = UserChangeForm
    add_form = UserCreationForm

    # Fields shown in detail view
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (_("Permissions"), {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        #(_("User info"), {"fields": ("native_name", "phone_no")}),  # custom fields
    )

    # Fields shown when creating a new user
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2"),
        }),
    )

    # Fields shown in the list view
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        # "native_name",
        # "phone_no",
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)


# Register the custom User model with custom admin
admin.site.register(AppUser, UserAdmin)
