from secrets import choice
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
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = [
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    ]

    GENRE_ADVENTURE = "adventrue"
    GENRE_CLASSICS = "classics"
    GENRE_CRIME = "crime"
    GENRE_FANTASY = "fantasy"
    GENRE_HORROR = "horror"
    GENRE_MYSTERY = "mystery"
    GENRE_NONFICTION = "nonfiction"
    GENRE_POETRY = "poetry"
    GENRE_ROMANCE = "romance"
    GENRE_SCIFIC = "sci-fi"

    GENRE_COMEDY = "comedy"
    GENRE_DRAMA = "drama"
    GENRE_HISTORY = "history"
    GENRE_ACTION = "action"
    GENRE_THRILLER = "thriller"
    GENRE_BIOGRAPHY = "biography"
    GENRE_WAR = "war"

    BOOK_GENRE = [
        (GENRE_ADVENTURE, "Adventure"),
        (GENRE_CLASSICS, "Classics"),
        (GENRE_CRIME, "Crime"),
        (GENRE_FANTASY, "Fantasy"),
        (GENRE_HORROR, "Horror"),
        (GENRE_MYSTERY, "Mystery"),
        (GENRE_NONFICTION, "Nonfiction"),
        (GENRE_POETRY, "Poetry"),
        (GENRE_ROMANCE, "Romance"),
        (GENRE_SCIFIC, "Sci-Fi"),
    ]

    MOVIE_GENRE = [
        (GENRE_ACTION, "Action"),
        (GENRE_ADVENTURE, "Adventure"),
        (GENRE_BIOGRAPHY, "Biography"),
        (GENRE_COMEDY, "Comedy"),
        (GENRE_DRAMA, "Drama"),
        (GENRE_FANTASY, "Fantasy"),
        (GENRE_HISTORY, "History"),
        (GENRE_HORROR, "Horror"),
        (GENRE_MYSTERY, "Mystery"),
        (GENRE_ROMANCE, "Romance"),
        (GENRE_THRILLER, "Thriller"),
        (GENRE_SCIFIC, "Sci-Fi"),
        (GENRE_WAR, "War"),
    ]

    bio = models.TextField(default="", null=True, blank=True)
    preference = models.CharField(
        choices=PREFERENCE_CHOICES, max_length=6, null=True, blank=True
    )
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    favourite_book_genre = models.CharField(
        choices=BOOK_GENRE, max_length=20, null=True, blank=True
    )
    favourite_movie_genre = models.CharField(
        choices=MOVIE_GENRE, max_length=20, null=True, blank=True
    )
