from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    """Custom Book Admin"""

    list_display = (
        "title",
        "year",
        "rating",
        "rating_average",
        "get_thumbnail",
    )

    list_filter = (
        "year",
        "rating",
        "category",
    )

    raw_id_fields = (
        "category",
        "writer",
    )

    search_fields = ("title",)

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="100px" src="{obj.cover_image.url}" />')

    get_thumbnail.short_description = "Thumbnail"
