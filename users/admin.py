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
        "favourite_book_genre",
        "favourite_movie_genre",
    )

    list_filter = [
        "language",
        "preference",
        "favourite_book_genre",
        "favourite_movie_genre",
    ]

    fieldsets = UserAdmin.fieldsets + (
        (
            "Preferences",
            {
                "fields": (
                    "preference",
                    "favourite_book_genre",
                    "favourite_movie_genre",
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
