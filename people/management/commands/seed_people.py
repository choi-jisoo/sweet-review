from django.core.management.base import BaseCommand
from django_seed import Seed
from people import models as people_models
from random import randint


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--total", type=int, default=1)

    def handle(self, *args, **options):
        total = options.get("total")
        if total <= 0:
            self.stdout.write(self.style.ERROR("Please enter a valid number."))
            return
        seeder = Seed.seeder()
        seeder.add_entity(
            people_models.Person,
            total,
            {
                "name": lambda x: seeder.faker.name(),
                "photo": lambda x: f"/people/{randint(1,20)}.jpg",
            },
        )
        seeder.execute()
