from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    TagsView,
    IngdientsView,
    RecipesViewset
)

router_v1 = DefaultRouter()
router_v1.register('tags', TagsView, basename='tags')
router_v1.register('ingredients', IngdientsView, basename='ingredients')
router_v1.register('recipes', RecipesViewset, basename='recipes')

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
