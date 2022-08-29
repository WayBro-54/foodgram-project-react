from email.policy import default
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
        fields = ('email', 'username', 'password')


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


class IngredientRecipesSerialiser(serializers.ModelSerializer):

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
    is_favorited = serializers.SerializerMethodField(default=False)
    #is_in_shopping_cart = serializers.SerializerMethodField()
    # tags = TagsSerialiser()
    # ingridients = IngredientsSerialier(
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = Recipes
        fields = (
            #    'tags',
            'author',
            # 'ingridients',
            'is_favorited',
            # 'is_in_shopping_cart',
            'name',
            'image',
            'text',
            'cooking_time'
        )
        read_only = '__all__'

    def get_is_favorited(self, obj):
        return True
