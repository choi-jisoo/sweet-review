from django.db import models
from core.models import TimeStampedModel

"""
- Book:
    title
    year
    category (ForeignKey => categories.Category)
    cover_image
    rating
    writer (ForeignKey => people.Person)
"""


class Book(TimeStampedModel):

    "Book Model Definition"

    title = models.CharField(max_length=150)
    year = models.IntegerField()
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="books"
    )
    cover_image = models.ImageField()
    rating = models.FloatField()
    writer = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="books"
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
