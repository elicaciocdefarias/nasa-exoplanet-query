from django.core.management.base import BaseCommand
from dynaconf import settings
from pathlib import PurePath
import subprocess


class Command(BaseCommand):
    def add_arguments(self, parser):
        ...

    def handle(self, *args, **kwargs):
        file_path = PurePath(settings.BASE_DIR).joinpath(
            "search/static/search/bootstrap-5.0.2/"
        )
        subprocess.run(
            [
                "./node_modules/.bin/npm-run-all",
                "css-compile",
                "css-prefix",
                "css-rtl",
                "css-minify",
            ],
            cwd=file_path,
        )
        subprocess.run(
            [
                "./node_modules/.bin/npm-run-all",
                "js-compile",
                "js-minify",
            ],
            cwd=file_path,
        )
