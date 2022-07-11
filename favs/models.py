from django.db import models
from core.models import TimeStampedModel

"""
- FavList
    created_by (OneToOne => users.User)
    books (ManyToMany => books.Book)
    movies (ManyToMany => movies.Movie)
"""


class FavList(TimeStampedModel):

    """Favourite List Model Definition"""

    created_by = models.OneToOneField("users.User", on_delete=models.CASCADE)
    books = models.ManyToManyField(
        "books.Book",
        related_name="fav_lists",
        blank=True,
        null=True,
    )
    movies = models.ManyToManyField(
        "movies.Movie",
        related_name="fav_lists",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Favourite List"

    def __str__(self):
        return f"{self.created_by}'s Fav List"
