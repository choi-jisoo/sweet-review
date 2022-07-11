from django.core.management.base import BaseCommand
from django.db.models import Q
from users import models as user_models
from django_seed import Seed
from random import choice
from categories import models as cat_models


class Command(BaseCommand):
    help = "This command creates users"

    def add_arguments(self, parser):
        parser.add_argument("--total", type=int, default=1)

    def handle(self, *args, **options):
        total = options.get("total", 1)

        seeder = Seed.seeder()
        book_categories = cat_models.Category.objects.filter(
            ~Q(kind=cat_models.Category.KIND_MOVIE)
        )
        movie_categories = cat_models.Category.objects.filter(
            ~Q(kind=cat_models.Category.KIND_BOOK)
        )
        seeder.add_entity(
            user_models.User,
            total,
            {
                "is_staff": False,
                "is_superuser": False,
                "favourite_book_category": lambda x: choice(book_categories),
                "favourite_movie_category": lambda x: choice(movie_categories),
            },
        )
        seeder.execute()
