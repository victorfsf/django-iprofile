# -*- coding: utf-8 -*-

from django.core.management import BaseCommand
from iprofile.cli import Shell


class Command(BaseCommand):

    help = 'Runs a IProfile IPython shell.'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)

    def handle(self, **options):
        Shell.run(options)
