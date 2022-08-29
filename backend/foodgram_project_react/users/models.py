
from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


USER = 'user'
ADMIN = 'admin'


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users mist have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save()

        return user


class UserAccount(AbstractUser):
    email = models.EmailField(
        max_length=255,
        unique=True
    )
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
# class User(AbstractUser, PermissionsMixin):
#     ROLES = (
#         (USER, USER),
#         (ADMIN, ADMIN),
#     )

#     username = models.CharField(
#         max_length=255,
#         unique=True,

#     )
#     email = models.EmailField(
#         max_length=255,
#         unique=True
#     )
#     first_name = models.CharField(max_length=150, blank=True)
#     last_name = models.CharField(max_length=150, blank=True)
#     bio = models.TextField(blank=True,)
#     role = models.CharField(
#         max_length=max(len(role) for role, _ in ROLES),
#         choices=ROLES,
#         default=USER
#     )
#     confirmation_code = models.CharField(
#         max_length=15,
#         blank=True,
#         null=True
#     )
#     objects = UserAccountManager

#     class Meta:
#         ordering = ('username',)
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['username', 'email'],
#                 name='уникальные пользователи'
#             )
#         ]
