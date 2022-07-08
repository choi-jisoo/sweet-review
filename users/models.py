from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """Custom Uer Model"""

    PREFERENCE_BOOKS = "books"
    PREFERENCE_MOVIES = "movies"

    PREFERENCE_CHOICES = [
        (PREFERENCE_BOOKS, "Books"),
        (PREFERENCE_MOVIES, "Movies"),
    ]

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_JAPANESE = "ja"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = [
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_JAPANESE, "Japanese"),
        (LANGUAGE_KOREAN, "Korean"),
    ]

    bio = models.TextField()
    preference = models.CharField(
        choices=PREFERENCE_CHOICES, max_length=6, null=True, blank=True
    )
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    favourite_book_cat = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="book_users",
    )
    favourite_movie_cat = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="movie_users",
    )

    def __str__(self):
        return self.username
