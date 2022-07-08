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
    cover_image = models.ImageField()
    rating = models.FloatField()
    category = models.ManyToManyField("categories.Category", related_name="movies")
    director = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="movies"
    )
    cast = models.ManyToManyField("people.Person")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
