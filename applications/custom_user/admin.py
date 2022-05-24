from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


from .models import MyUser, Technology


class MyUserAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "phone",
        "first_name",
        "last_name",
        "is_staff",
        "get_avatar"
    )
    list_display_links = ('id', 'username', 'email',)
    search_fields = ('username', 'email')
    readonly_fields = ('email', 'last_login', 'date_joined', 'get_avatar',)
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
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_("Дополнительная информация"), {"fields": ("phone", "avatar", "get_avatar", "gender")}),
        (_("Технологии"), {"fields": ("technology", )}),
    )
    save_as = True
    save_on_top = True

    def get_avatar(self, obj):
        """Отобразим фото в админке"""

        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="100">')
        else:
            return f'Аватар не установлен'

    get_avatar.short_description = 'Аватар'


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    fields = ('name', )
    save_as = True


admin.site.register(MyUser, MyUserAdmin)
