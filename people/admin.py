from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):

    """Custon Person Admin"""

    list_display = (
        "name",
        "kind",
        "get_thumbnail",
    )

    list_filter = ("kind",)

    search_fields = ("name",)

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="100px" src="{obj.photo.url}" />')

    get_thumbnail.short_description = "Thumbnail"
