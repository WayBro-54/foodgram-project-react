from rest_framework import viewsets, mixins
from recept.models import (
    Tags,
    Recipes,
    Ingredients,
    UserAccount
)
from .serialisers import (
    TagsSerialiser,
    IngredientsSerialier,
    IngredientRecipesSerialiser,
    RecipesSerialiser,
    UserSerialiser
)


class UserViewset(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserSerialiser


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
    serializer_class = IngredientRecipesSerialiser
    queryset = Ingredients.objects.all()
