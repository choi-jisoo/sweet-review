from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    list_display = (
        "username",
        "language",
        "preference",
        "favourite_book_category",
        "favourite_movie_category",
    )

    list_filter = (
        "language",
        "preference",
        "favourite_book_category",
        "favourite_movie_category",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Preferences",
            {
                "fields": (
                    "preference",
                    "favourite_book_category",
                    "favourite_movie_category",
                ),
            },
        ),
        (
            "Others",
            {
                "fields": (
                    "bio",
                    "language",
                ),
            },
        ),
    )
