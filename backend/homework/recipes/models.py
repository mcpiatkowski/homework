from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=70, default='', blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=70, default='', blank=True)
    description = models.TextField(null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name
