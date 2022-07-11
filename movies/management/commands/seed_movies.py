from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from movies import models as movie_models
from django_seed import Seed
from random import randint, choice, uniform
from categories import models as cat_models
from people import models as people_models


class Command(BaseCommand):
    help = "This command creates movies"

    def add_arguments(self, parser):
        parser.add_argument("--total", type=int, default=1)

    def handle(self, *args, **options):
        total = options.get("total", 1)

        seeder = Seed.seeder()
        all_categories = cat_models.Category.objects.filter(
            kind=cat_models.Category.KIND_MOVIE
        ).all()
        all_directors = people_models.Person.objects.filter(
            kind=people_models.Person.KIND_DIRECTOR
        ).all()
        seeder.add_entity(
            movie_models.Movie,
            total,
            {
                "year": lambda x: randint(1970, 2022),
                "cover_image": lambda x: f"/movie_images/{randint(1,14)}.jpg",
                "rating": lambda x: round(uniform(0, 5), 2),
                "category": lambda x: choice(all_categories),
                "director": lambda x: choice(all_directors),
            },
        )
        created_movies = seeder.execute()
        created_clean = flatten(list(created_movies.values()))
        all_casts = people_models.Person.objects.filter(
            kind=people_models.Person.KIND_ACTOR
        ).all()
        for pk in created_clean:
            movie = movie_models.Movie.objects.get(pk=pk)
            magic_number1 = randint(0, all_casts.count() - 1)
            for n in range(all_casts.count()):
                if n == magic_number1:
                    movie.cast.add(all_casts[n])
                magic_number2 = randint(0, 15)
                if magic_number2 < 3:
                    movie.cast.add(all_casts[n])
