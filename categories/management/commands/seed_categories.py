from django.core.management.base import BaseCommand
from categories import models as cat_models


KEYWORD = "categories"


class Command(BaseCommand):
    def handle(self, *args, **options):
        book_cat = [
            "Biography",
            "Classics",
            "Comic",
            "Essay",
            "Graphic Novel",
            "Historical Fiction",
            "History",
            "Literary Fiction",
            "Poetry",
            "Self-Help",
        ]
        movie_cat = [
            "Comedy",
            "Documentary",
            "Drama",
            "Western",
        ]
        both_cat = [
            "Action & Adventure",
            "Detective",
            "Mystery",
            "Fantasy",
            "Horror",
            "Romance",
            "Sci-Fi",
            "Suspense",
            "Thrillers",
        ]
        for book in book_cat:
            cat_models.Category.objects.create(
                name=book, kind=cat_models.Category.KIND_BOOK
            )

        for movie in movie_cat:
            cat_models.Category.objects.create(
                name=movie, kind=cat_models.Category.KIND_MOVIE
            )

        for both in both_cat:
            cat_models.Category.objects.create(
                name=both, kind=cat_models.Category.KIND_BOTH
            )
