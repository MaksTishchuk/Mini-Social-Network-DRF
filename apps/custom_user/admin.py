from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


from custom_user.models import MyUser


class MyUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "phone",
        "first_name",
        "last_name",
        "is_staff"
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "middle_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("first_login", "last_login", "date_joined")}),
        (_("Additional info"), {"fields": ("phone", "avatar", "gender")}),
    )


admin.site.register(MyUser, MyUserAdmin)