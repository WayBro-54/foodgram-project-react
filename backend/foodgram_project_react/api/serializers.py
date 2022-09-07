
# from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.serializers import UserAccountViewset
from .validators import validate_username
from .models import (
    AmountIngredients,
    Ingredients,
    Recipes,
    Tags,
    Follow,
    # IngredientsAmout
)
from users.models import UserAccount
User = get_user_model()


class UsernameValidationMixin:
    """Миксин-валидатор лоя поля username."""

    def validate_username(self, value):
        return validate_username(value)


class UserSerializer(serializers.ModelSerializer, UsernameValidationMixin):
    """"""
    class Meta:
        model = UserAccount
        fields = (

        )

# class UserCreateSerialiser(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = (
#             'email',
#             'id',
#             'username',
#             'password',
#             'first_name',
#             'last_name'
#         )

# class UserSerialiser(UserSerializer):
#     is_subscribed = serializers.SerializerMethodField()

#     def get_is_subscribed(self, obj):
#         if self.context['request'].user:
#             return False
#         return Follow.objects.filter(
#             user=self.context['request'].user,
#             author=obj
#         )

#     class Meta:
#         model = User
#         fields =(
#             'email',
#             'id',
#             'username',
#             'first_name',
#             'last_name',
#             'is_subscribed'
#         )


# class PasswordSerializer(serializers.Serializer):
#     current_password = serializers.CharField(reqired=True)
#     new_password = serializers.CharField(reqired=True)

# class IngredientsAmoutSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = IngredientsAmout
#         fields = ('__all__')


class TagsSerializer(serializers.ModelSerializer):
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


class TagsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = (
            'id',
        )


class IngredientsSerializer(serializers.ModelSerializer):  # Done
    """Сериализотор модели Ingredients."""
    id = serializers.ReadOnlyField(source='ingredients_id.id')
    name = serializers.ReadOnlyField(source='ingredients_id.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredients_id.measurement_unit')

    class Meta:
        model = AmountIngredients
        fields = (
            'id',
            'name',
            'measurement_unit',

        )
        read_only = (
            'id',
            'name',
            'measurement_unit',

        )


class IngredientRecipesSerializer(serializers.ModelSerializer):  # Done
    """Сериализатор для добавения рецептов."""

    class Meta:
        model = Ingredients
        fields = (
            'id',
            'amount'
        )


class RecipesCreateSerializer(serializers.ModelSerializer):
    tags = Tags

    class Meta:
        model = Recipes
        fields = (
            '__all__'
        )


class RecipesSerializer(serializers.ModelSerializer):
    """Сериализатор Модели Recipes, с безопасными методами."""
    is_favorited = serializers.SerializerMethodField(default=False)
    is_in_shopping_cart = serializers.SerializerMethodField()
    tags = TagsSerializer(many=True)
    ingridients = IngredientsSerializer(many=True)
    author = UserAccountViewset()

    class Meta:
        model = Recipes
        fields = (
            'id',
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

    def get_is_favorited(self, obj):
        if self.context['request'].user:
            return False
        return Follow.objects.filter(
            user=self.context['request'].user,
            author=obj
        ).exists()

    def get_is_in_shopping_cart(self, obj):
        if self.context['request'].user:
            return False
