from factory import django, fuzzy, Sequence
from faker import Factory

from core import models

factory_ru = Factory.create(locale="ru_Ru")


class Product(django.DjangoModelFactory):
    name = Sequence(lambda n: factory_ru.word())
    description = Sequence(lambda n: factory_ru.word())
    cost = fuzzy.FuzzyInteger(100, 1000)

    class Meta:
        model = models.Product
