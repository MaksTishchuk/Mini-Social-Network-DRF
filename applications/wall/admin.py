from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Посты """

    list_display = ("id", "user", "create_date", "published", "moderation", "view_count")
    list_display_links = ("id", "user")
    fields = ("text", "create_date", "published", "moderation", "view_count", "user", )
    readonly_fields = ("create_date", "view_count", "user", )
    save_as = True


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """ Коментарии к постам """
    list_display = ("user", "post", "created_date", "update_date", "published", "id")
    list_display_links = ("id", "user", "post",)
    mptt_level_indent = 15
