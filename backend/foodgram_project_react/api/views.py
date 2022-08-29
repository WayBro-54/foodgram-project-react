from rest_framework import viewsets, mixins
from recept.models import (
    Tags,
    Recipes,
    Ingredients
)
from .serialisers import (
    TagsSerialiser,
    IngredientsSerialier,
    RecipesSerialiser
)


class ListObjectViewset(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    '''Вьюсет получения списка объектов и объекта.'''


class RecipesViewset(viewsets.ModelViewSet):
    model = Recipes
    serializer_class = RecipesSerialiser
    queryset = Recipes.objects.all()


class TagsView(ListObjectViewset):
    model = Tags
    serializer_class = TagsSerialiser
    queryset = Tags.objects.all()


class IngdientsView(ListObjectViewset):
    model = Ingredients
    serializer_class = IngredientsSerialier
    queryset = Ingredients.objects.all()
