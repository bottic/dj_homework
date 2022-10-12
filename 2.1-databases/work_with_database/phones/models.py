from django.db import models
from autoslug import AutoSlugField

class Phone(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True)
    price = models.FloatField(null=False)
    release_date = models.DateField(null=False)
    lte_exists = models.BooleanField(default=True)
    slug= AutoSlugField(populate_from='name', unique=True, editable=True)

    def __str__(self):
        return f'{self.name}: {self.price}'
