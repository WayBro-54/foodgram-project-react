from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Ingredients, Recipes, RecipesTags,
                     Tags, IngredientsAmout,  # UserAccount
                     )


class RecipesAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        # 'tags',
        'ingridients',
        'author',
        'name',
        'text',
        'cooking_time'
    )
    list_editable = ('ingridients',)
    search_fields = ('name',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Recipes, RecipesAdmin)
admin.site.register(Tags)
admin.site.register(Ingredients)
# admin.site.register(UserAccount)
