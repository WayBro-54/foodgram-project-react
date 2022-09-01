
# from djoser.serializers import UserCreateSerializer, UserSerializer
from dataclasses import field
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import (
    Ingredients,
    Recipes,
    Tags,
    Follow,
    IngredientsAmout
)
from users.models import UserAccount
User = get_user_model()


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

class IngredientsAmoutSerializers(serializers.ModelSerializer):
    class Meta:
        model = IngredientsAmout
        fields = ('__all__')


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
    amout = serializers.ReadOnlyField(source='ingridients_amout.amout')

    class Meta:
        model = Ingredients
        fields = (
            'id',
            'name',
            'measurement_unit',
            'amout'
        )


class IngredientRecipesSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Ingredients
        fields = (
            'id',
            'name',
            'measurement_unit'

        )


class RecipesSerialiser(serializers.ModelSerializer):
    """Сериализатор Модели Recipes, с безопасными методами."""
    is_favorited = serializers.SerializerMethodField(default=False)
    is_in_shopping_cart = serializers.SerializerMethodField()
    tags = TagsSerialiser(many=True)
    ingridients = IngredientsSerialier()

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
