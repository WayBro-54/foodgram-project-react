
from dataclasses import field
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from recept.models import (
    Ingredients,
    Recipes,
    Tags,
    Follow
)
from users.models import UserAccount
User = get_user_model()


class UserCreateSerialiser(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'email',
            'id',
            'username',
            'password',
            'first_name',
            'last_name'
        )

class UserSerialiser(UserSerializer):
    is_subscribed = serializers.SerializerMethodField()

    def get_is_subscribed(self, obj):
        if self.context['request'].user:
            return False
        return Follow.objects.filter(
            user=self.context['request'].user,
            author=obj
        )

    class Meta:
        model = User
        fields =(
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed'
        )


class PasswordSerializer(serializers.Seializer):
    current_password = serializers.CharField(reqired=True)
    new_password = serializers.CharField(reqired=True)


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
            'measurement_unit',
            'amout'
        )



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
            # 'is_favorited',
            # 'is_in_shopping_cart',
            'name',
            'image',
            'text',
            'cooking_time'
        )
        read_only = '__all__'

    def get_is_favorited(self, obj):
        if self.context.get['request']:
            return False
        
            
            
