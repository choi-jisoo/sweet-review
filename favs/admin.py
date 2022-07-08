from django.contrib import admin
from . import models


@admin.register(models.FavList)
class FavListAdmin(admin.ModelAdmin):

    """Custom Favourite List Admin"""

    list_display = ("created_by", "count_books", "count_movies")

    filter_horizontal = (
        "books",
        "movies",
    )

    def count_books(self, obj):
        return obj.books.count()

    count_books.short_description = "Count of books"

    def count_movies(self, obj):
        return obj.movies.count()

    count_movies.short_description = "Count of movies"
