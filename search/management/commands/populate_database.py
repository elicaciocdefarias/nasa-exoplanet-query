from search.handlers import HandleRequestExoplanetArchive
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        ...

    def handle(self, *args, **kwargs):
        request = HandleRequestExoplanetArchive()

        start = 0
        count = 100
        amount = 29500
        for _ in range(0, amount, count):
            self.stdout.write(
                self.style.SUCCESS(f"baixando de {start} até {(start+count)}...")
            )
            r = request.get(start)
            start = start + count
            self.stdout.write(self.style.SUCCESS(r.headers))
