from django.contrib import admin

from .models import (
    Recipes,
    Tags,
    Ingredients,
    Follow,
    RecipesTags,
    UserAccount,
    AmountIngredients
)


# class TagsAdmin(admin.TabularInline):
#     model = Recipes.


class AdminSite(admin.ModelAdmin):
    fields = (
        # 'tags',
        'ingridients',
        'author',
        'name',
        'text',
        'cooking_time'
    )
    # inlines = (
    #     TagsAdmin,
    # )


admin.site.register(Recipes, AdminSite)
admin.site.register(Tags)
admin.site.register(Ingredients)
admin.site.register(AmountIngredients)
admin.site.register(Follow)
admin.site.register(RecipesTags)
admin.site.register(UserAccount)
