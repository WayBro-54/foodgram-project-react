from django.contrib import admin

from users.models import UserAccount, Subscribe
from .models import (Favorite, Ingredient, IngredientRecipe,
                     Recipe, ShoppingCart, Tag)


EMPTY_VALUE = '-пусто-'


@admin.register(UserAccount)
class UserAdmin(admin.ModelAdmin):
    """Представляет модель User в интерфейсе администратора."""
    list_display = ('id', 'username', 'first_name',
                    'last_name', 'email', 'password')
    list_filter = ('email', 'username', )
    empty_value_display = EMPTY_VALUE


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    """Представляет модель Subscribe в интерфейсе администратора."""
    list_display = ('id', 'user', 'author')
    search_fields = ('user',)
    list_filter = ('user', )
    empty_value_display = EMPTY_VALUE


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Представляет модель Tag в интерфейсе администратора."""
    list_display = ('id', 'name', 'color', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = EMPTY_VALUE


class IngredientRecipeInline(admin.TabularInline):
    """Представляет модель IngredientRecipe в интерфейсе администратора."""
    model = IngredientRecipe


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Представляет модель Ingredient в интерфейсе администратора."""
    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('name',)
    inlines = (IngredientRecipeInline,)
    empty_value_display = EMPTY_VALUE


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Представляет модель Recipe в интерфейсе администратора."""
    list_display = ('id', 'name', 'author')
    search_fields = ('author', 'name', 'tags')
    inlines = (IngredientRecipeInline,)
    empty_value_display = EMPTY_VALUE

    def is_favorited(self, obj):
        return Favorite.objects.filter(recipe=obj).count()


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Представляет модель Favorite в интерфейсе администратора."""
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = EMPTY_VALUE


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Представляет модель ShoppingCart в интерфейсе администратора."""
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = EMPTY_VALUE
