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
        "favourite_book_cat",
        "favourite_movie_cat",
    )

    list_filter = (
        "language",
        "preference",
        "favourite_book_cat",
        "favourite_movie_cat",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Preferences",
            {
                "fields": (
                    "preference",
                    "favourite_book_cat",
                    "favourite_movie_cat",
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
