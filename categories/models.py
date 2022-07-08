from django.db import models
from core.models import TimeStampedModel

"""
- Category
    name
    kind (book/movie/both)
"""


class Category(TimeStampedModel):

    """Category Model Definition"""

    KIND_BOOK = "book"
    KIND_MOVIE = "movie"
    KIND_BOTH = "both"

    KING_CHOICES = (
        (KIND_BOOK, "Book"),
        (KIND_MOVIE, "Movie"),
        (KIND_BOTH, "both"),
    )

    name = models.CharField(max_length=30)
    kind = models.CharField(choices=KING_CHOICES, max_length=10)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
