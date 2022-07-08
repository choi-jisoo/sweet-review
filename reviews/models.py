from django.db import models
from core.models import TimeStampedModel

"""
- Review
    created_by (ForeignKey => users.User)
    text
    movie (ForeignKey => movies.Movie, null,blank)
    book (ForeignKey => movies.Movie, null,blank)
    rating
"""


class Review(TimeStampedModel):

    """Review Model Definition"""

    created_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
    text = models.TextField()
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    rating = models.IntegerField()

    def __str__(self):
        return self.text
