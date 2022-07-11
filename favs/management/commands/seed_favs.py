from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from random import randint, choice
from favs.models import FavList
from users import models as user_models
from movies import models as movie_models
from books import models as book_models


class Command(BaseCommand):
    help = "This command creates favourite lists"

    def add_arguments(self, parser):
        parser.add_argument("--total", type=int, default=1)

    def handle(self, *args, **options):
        total = options.get("total", 1)

        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        seeder.add_entity(
            FavList,
            total,
            {
                "created_by": lambda x: choice(all_users),
            },
        )
        created_favs = seeder.execute()
        created_clean = flatten(list(created_favs.values()))
        all_movies = movie_models.Movie.objects.all()
        all_books = book_models.Book.objects.all()

        for pk in created_clean:
            favlist = FavList.objects.get(pk=pk)

            magic_movie_number = randint(0, all_movies.count() - 1)
            for n in range(all_movies.count()):
                if n == magic_movie_number:
                    favlist.movies.add(all_movies[n])
                else:
                    magic_number = randint(0, 15)
                    if magic_number < 3:
                        favlist.movies.add(all_movies[n])

            magic_book_number = randint(0, all_books.count() - 1)
            for n in range(all_books.count()):
                if n == magic_book_number:
                    favlist.books.add(all_books[n])
                else:
                    magic_number = randint(0, 15)
                    if magic_number < 3:
                        favlist.books.add(all_books[n])
