from search.handlers import HandleExoplanetArchive
from django.core.management.base import BaseCommand
from search.models import Exoplanet


class Command(BaseCommand):
    def add_arguments(self, parser):
        ...

    def handle(self, *args, **kwargs):
        exoplanet_archive = HandleExoplanetArchive()
        records = exoplanet_archive.read().normalize().records()

        for kwargs in records:
            Exoplanet.objects.update_or_create(**kwargs)
