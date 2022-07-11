from django.db import models
from core.models import TimeStampedModel

"""
- Movie:
    title
    year
    cover_image
    rating
    category (ManyToMany => categories.Category)
    director (ForeignKey => people.Person)
    cast (ManyToMany => people.Person)
"""


class Movie(TimeStampedModel):

    """Movie Model Definition"""

    title = models.CharField(max_length=150)
    year = models.IntegerField()
    cover_image = models.ImageField(upload_to="movie_images", null=True, blank=True)
    rating = models.FloatField()
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="movies"
    )
    director = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="movies"
    )
    cast = models.ManyToManyField("people.Person", blank=True, null=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def rating_average(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating
        return round(all_ratings / len(all_reviews), 2) if len(all_reviews) > 0 else 0
