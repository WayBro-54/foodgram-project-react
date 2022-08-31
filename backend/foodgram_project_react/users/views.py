from django.contrib.auth import get_user_model
from djoser import views

User = get_user_model()

class UserAccountViewset(views.UserViewSet):
    def get_queryset(self):
        return User.objects.all()
