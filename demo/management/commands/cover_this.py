from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Do nothing command to demo coverage 6 / django issues'

    def handle(self, *args, **options):
        print('Hello, world!')
