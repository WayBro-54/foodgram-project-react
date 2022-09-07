from rest_framework import viewsets, mixins
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,

)

from .models import (
    Tags,
    Recipes,
    Ingredients,
)
from .serializers import (
    TagsSerializer,
    TagsCreateSerializer,
    IngredientsSerializer,
    IngredientRecipesSerializer,
    RecipesSerializer,
    RecipesCreateSerializer
)


class ListObjectViewset(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    '''Вьюсет получения списка объектов и объекта.'''


class RecipesViewset(viewsets.ModelViewSet):
    serializer_class = RecipesSerializer
    queryset = Recipes.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ['list', 'retriver']:
            return RecipesSerializer
        return RecipesCreateSerializer


class TagsView(ListObjectViewset):
    """Представление Tags.
    Только GET запросы."""
    serializer_class = TagsSerializer
    queryset = Tags.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class IngdientsView(ListObjectViewset):
    serializer_class = IngredientsSerializer
    queryset = Ingredients.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
