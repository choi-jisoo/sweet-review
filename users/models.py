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

    GENRE_ACTION = "action"
    GENRE_ADVENTURE = "adventure"
    GENRE_BIOGRAPHIES = "biographies"
    GENRE_CLASSICS_BOOK = "classics"
    GENRE_COMEDY_MOVIE = "comedy"
    GENRE_COMIC_BOOK = "comic"
    GENRE_COOKBOOKS_BOOK = "cookbooks"
    GENRE_DETECTIVE = "detective"
    GENRE_DOCUMENTARY_MOVIE = "documentary"
    GENRE_DRAMA_MOVIE = "drama"
    GENRE_ESSAYS_BOOK = "essays"
    GENRE_FANTASY = "fantasy"
    GENRE_FICTION_BOOK = "fiction"
    GENRE_HISTORY = "history"
    GENRE_HORROR = "horror"
    GENRE_MYSTERY = "mystery"
    GENRE_POETRY_BOOK = "poetry"
    GENRE_ROMANCE = "romance"
    GENRE_SCIFI = "sci-fi"
    GENRE_THRILLERS = "thrillers"
    GENRE_WESTERN_MOVIE = "western"

    GENRE_CHOICES = [
        (GENRE_ACTION, "Action"),
        (GENRE_ADVENTURE, "Adventure"),
        (GENRE_BIOGRAPHIES, "Biographies"),
        (GENRE_DETECTIVE, "Detective"),
        (GENRE_FANTASY, "Fantasy"),
        (GENRE_HISTORY, "History"),
        (GENRE_HORROR, "Horror"),
        (GENRE_MYSTERY, "Mystery"),
        (GENRE_ROMANCE, "Romance"),
        (GENRE_SCIFI, "Sci-Fi"),
        (GENRE_THRILLERS, "Thrillers"),
    ]

    BOOK_GENRE_CHOICES = GENRE_CHOICES + [
        (GENRE_CLASSICS_BOOK, "Classics"),
        (GENRE_COMIC_BOOK, "Comic"),
        (GENRE_COOKBOOKS_BOOK, "Cookbooks"),
        (GENRE_ESSAYS_BOOK, "Essays"),
        (GENRE_FICTION_BOOK, "Fiction"),
        (GENRE_POETRY_BOOK, "Poetry"),
    ]
    BOOK_GENRE_CHOICES.sort()

    MOVIE_GENRE_CHOICES = GENRE_CHOICES + [
        (GENRE_COMEDY_MOVIE, "Comedy"),
        (GENRE_DOCUMENTARY_MOVIE, "Documentary"),
        (GENRE_DRAMA_MOVIE, "Drama"),
        (GENRE_WESTERN_MOVIE, "Western"),
    ]
    MOVIE_GENRE_CHOICES.sort()

    bio = models.TextField(default="", null=True, blank=True)
    preference = models.CharField(
        choices=PREFERENCE_CHOICES, max_length=6, null=True, blank=True
    )
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    favourite_book_genre = models.CharField(
        choices=BOOK_GENRE_CHOICES, max_length=20, null=True, blank=True
    )
    favourite_movie_genre = models.CharField(
        choices=MOVIE_GENRE_CHOICES, max_length=20, null=True, blank=True
    )
