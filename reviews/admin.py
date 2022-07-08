from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """Custom Review Admin"""

    list_display = (
        "created_by",
        "movie",
        "book",
        "rating",
    )

    list_filter = (
        "movie",
        "book",
    )

    raw_id_fields = (
        "created_by",
        "movie",
        "book",
    )
