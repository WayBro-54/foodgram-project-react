from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from recept.models import (
    Ingredients,
    Recipes,
    Tags,
)
User = get_user_model()


class UserSerialiser(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('email', 'name', 'password')


class TagsSerialiser(serializers.ModelSerializer):
    """Сериализатор модели Tags"""
    class Meta:
        model = Tags
        fields = (
            'id',
            'name',
            'color',
            'slug'
        )
        read_only = ('__all__')


class IngredientsSerialier(serializers.ModelSerializer):
    """Сериализотор модели Ingredients."""

    class Meta:
        model = Ingredients
        fields = (
            'id',
            'name',
            'measurement_unit'
        )
        read_only = ('__all__')


class RecipesSerialiser(serializers.ModelSerializer):
    """Сериализатор Модели Recipes, с безопасными методами."""
    is_favorited = serializers.BooleanField()
    is_in_shopping_cart = serializers.BooleanField()
    tags = TagsSerialiser()

    class Meta:
        model = Recipes
        fields = (
            'tags',
            'author',
            'ingridients',
            'is_favorited',
            'is_in_shopping_cart',
            'name',
            'image',
            'text',
            'cooking_time'
        )
        read_only = '__all__'
