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
    cover_image = models.ImageField(upload_to="book_images", null=True, blank=True)
    rating = models.FloatField()
    writer = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="books"
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def rating_average(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating
        return all_ratings / len(all_reviews) if len(all_reviews) > 0 else 0
