from django.db import models
from core.models import TimeStampedModel

"""
- Person
    name
    kind (choice=Actor/Director/Writer)
    photo
"""


class Person(TimeStampedModel):

    """Person Model Definition"""

    KIND_ACTOR = "actor"
    KIND_DIRECTOR = "director"
    KIND_WRITER = "writer"

    KIND_CHOICES = (
        (KIND_ACTOR, "Actor"),
        (KIND_DIRECTOR, "Director"),
        (KIND_WRITER, "Writer"),
    )

    name = models.CharField(max_length=30)
    kind = models.CharField(choices=KIND_CHOICES, max_length=10, blank=True)
    photo = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.name
