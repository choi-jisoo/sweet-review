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

    KIND_CHOICES = (
        (KIND_BOOK, "Book"),
        (KIND_MOVIE, "Movie"),
        (KIND_BOTH, "Both"),
    )

    name = models.CharField(max_length=30)
    kind = models.CharField(choices=KIND_CHOICES, max_length=10)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)
