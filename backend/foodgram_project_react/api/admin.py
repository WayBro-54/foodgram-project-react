from django.contrib import admin

from .models import (
    Recipes,
    Tags,
    Ingredients,
    Follow,
    RecipesTags,
    UserAccount
)


# class TagsAdmin(admin.TabularInline):
#     model = Recipes.


class AdminSite(admin.ModelAdmin):
    fields = (
        # 'tags',
        'ingridients',
        'author',
        'name',
        'text'
    )
    # inlines = (
    #     TagsAdmin,
    # )


admin.site.register(Recipes, AdminSite)
admin.site.register(Tags)
admin.site.register(Ingredients)
# admin.site.register(IngredientsAmout)
admin.site.register(Follow)
admin.site.register(RecipesTags)
admin.site.register(UserAccount)
