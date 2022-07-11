from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from random import randint, choice
from reviews.models import Review
from users import models as user_models
from movies import models as movie_models
from books import models as book_models


class Command(BaseCommand):
    help = "This command creates favourite reviews"

    def add_arguments(self, parser):
        parser.add_argument("--total", type=int, default=1)

    def handle(self, *args, **options):
        total = options.get("total", 1)
        all_users = user_models.User.objects.all()
        all_books = book_models.Book.objects.all()
        all_movies = movie_models.Movie.objects.all()

        for i in range(total):

            seeder = Seed.seeder()
            seeder.add_entity(
                Review,
                1,
                {
                    "created_by": lambda x: choice(all_users),
                    "rating": lambda x: randint(0, 5),
                    "book": lambda x: choice(all_books) if randint(0, 1) == 0 else None,
                },
            )
            created_reviews = seeder.execute()
            created_clean = flatten(list(created_reviews.values()))

            review = Review.objects.get(pk=created_clean[0])
            if not review.book:
                review.delete()
                seeder = Seed.seeder()
                seeder.add_entity(
                    Review,
                    1,
                    {
                        "created_by": lambda x: choice(all_users),
                        "rating": lambda x: randint(0, 5),
                        "movie": lambda x: choice(all_movies),
                    },
                )
                seeder.execute()
