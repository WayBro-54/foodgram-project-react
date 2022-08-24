from django.db import models

from users.models import User


class Recipes(models.model):
    tags = models.ManyToManyField()
    author = models.ForeignKey(
        'User'
    )
    ingridients = models.ForeignKey(
        'Ingredients',
        on_delete=models.CASCADE,
        related_name='ingridients',
        verbose_name='Ингридиенты'
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    text = models.TextField()
    cooking_time = models.IntegerField()

    class Meta:
        verbose_name = 'Рецепты'
        verbose_name_plural = 'Рецепты'

    def __str__(self) -> str:
        return self.name


class Tags(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Тег'
    )
    color = models.CharField(
        max_length=7,
        verbose_name='Цветовой HEX-код'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True
    )

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'


class Ingredients(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Ингридиент'
    )
    measurement_unit = models.CharField(
        max_length=25,
        verbose_name='Единица измерения'
    )
    ingridients_amout = models.ForeignKey(
        'IngredientsAmout',
        on_delete=models.CASCADE,
        related_name='amout'
    )


class IngredientsAmout(models.Model):
    amout = models.FloatField()
