from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    """Custom Book Admin"""

    list_display = (
        "title",
        "year",
        "rating",
    )

    list_filter = (
        "year",
        "rating",
        "category",
    )
