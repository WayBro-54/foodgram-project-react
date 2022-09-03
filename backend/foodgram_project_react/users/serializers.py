from django.contrib.auth import get_user_model

from djoser.conf import settings
from djoser.serializers import UserCreateSerializer

User = get_user_model()


class UserAccountViewset(UserCreateSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            'password',
            'username'
        )


class UserAccountIdViewset(UserCreateSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            'username',
            # settings.USER_ID_FIELDS
        )
