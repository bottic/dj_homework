import csv
from autoslug import AutoSlugField
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            Phone(
                id=int(phone['id']),
                name=phone['name'],
                image=phone['image'],
                price=float(phone['price']),
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                # slug=AutoSlugField(populate_from='name', unique=True, editable=True)
            ).save()

