from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):

    """Custom Movie Admin"""

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
    )

    search_fields = ("title",)

    raw_id_fields = ("director",)

    filter_horizontal = (
        "category",
        "cast",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="100px" src="{obj.cover_image.url}" />')

    get_thumbnail.short_description = "Thumbnail"
