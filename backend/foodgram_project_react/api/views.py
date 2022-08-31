from rest_framework import viewsets, mixins
from recept.models import (
    Tags,
    Recipes,
    Ingredients,
)
from .serialisers import (
    TagsSerialiser,
    IngredientsSerialier,
    IngredientRecipesSerialiser,
    RecipesSerialiser,
)


class ListObjectViewset(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    '''Вьюсет получения списка объектов и объекта.'''


class RecipesViewset(viewsets.ModelViewSet):
    serializer_class = RecipesSerialiser
    queryset = Recipes.objects.all()


class TagsView(ListObjectViewset):
    serializer_class = TagsSerialiser
    queryset = Tags.objects.all()


class IngdientsView(ListObjectViewset):
    serializer_class = IngredientsSerialier
    queryset = Ingredients.objects.all()
