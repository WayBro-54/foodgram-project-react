from django.contrib import admin

from .models import (
    Recipes,
    Tags,
    Ingredients,
    IngredientsAmout,
    Follow,
    RecipesTags,
    UserAccount
)


class AdminSite(admin.ModelAdmin):
    fields = (
        # 'tags',
        'author',
        'name',
        'text'
    )


admin.site.register(Recipes, AdminSite)
admin.site.register(Tags)
admin.site.register(Ingredients)
admin.site.register(IngredientsAmout)
admin.site.register(Follow)
admin.site.register(RecipesTags)
admin.site.register(UserAccount)
