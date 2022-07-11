from django.core.management.base import BaseCommand
from django.db.models import Q
from books import models as book_models
from django_seed import Seed
from random import randint, uniform, choice
from categories import models as cat_models
from people import models as people_models


class Command(BaseCommand):
    help = "This command creates books"

    def add_arguments(self, parser):
        parser.add_argument("--total", type=int, default=1)

    def handle(self, *args, **options):
        total = options.get("total", 1)

        seeder = Seed.seeder()
        all_categories = cat_models.Category.objects.filter(
            ~Q(kind=cat_models.Category.KIND_MOVIE)
        )
        all_writers = people_models.Person.objects.filter(
            kind=people_models.Person.KIND_WRITER
        ).all()
        seeder.add_entity(
            book_models.Book,
            total,
            {
                "year": lambda x: randint(1970, 2022),
                "cover_image": lambda x: f"/book_images/{randint(1,18)}.jpg",
                "rating": lambda x: round(uniform(0, 5), 2),
                "category": lambda x: choice(all_categories),
                "writer": lambda x: choice(all_writers),
            },
        )
        seeder.execute()
