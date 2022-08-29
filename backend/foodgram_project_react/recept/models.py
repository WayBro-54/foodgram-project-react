from django.db import models
from users.models import UserAccount


class Recipes(models.Model):
    tags = models.ManyToManyField(
        'Tags',
        through='RecipesTags',
        verbose_name='Теги'
    )
    author = models.ForeignKey(
        UserAccount,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name='Автор'
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
    image = models.ImageField(
        blank=True,
        verbose_name='Изображение'
    )
    text = models.TextField(
        verbose_name='Описание рецепта'
    )
    cooking_time = models.IntegerField(
        verbose_name='Время приготовления'
    )
    pub_date = models.DateTimeField(
        auto_now=True
    )

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
        unique=True,
        verbose_name='Слаг'
    )

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'

    def __str__(self) -> str:
        return f'{self.name} {self.color} {self.slug}'


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
        related_name='isamout',
        blank=True,
        verbose_name='Количество',
        null=True
    )

    class Meta:
        verbose_name = 'Ингредиенты'
        verbose_name_plural = 'Ингредиенты'


class IngredientsAmout(models.Model):
    amout = models.FloatField(
        null=True,
        verbose_name='Количество'
    )


class RecipesTags(models.Model):
    tags = models.ForeignKey(
        Tags,
        on_delete=models.DO_NOTHING,
        verbose_name='Теги'
    )
    recipes = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        verbose_name='Рецепты'
    )

    class Meta:
        verbose_name = 'Рецепты и теги'
        verbose_name_plural = 'Рецепты и теги'

    def __str__(self):
        return f'{self.tags}, {self.recipes}'


class Follow(models.Model):
    user = models.ForeignKey(
        UserAccount,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь'
    )
    author = models.ForeignKey(
        UserAccount,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'Последователи'
        verbose_name_plural = 'Последователи'
        constraints = [models.UniqueConstraint(
            fields=['user', 'author'], name='unique follow'
        )]

    def __str__(self):
        return f"Последователь: '{self.user}', автор: '{self.author}'"
