
from django.db import models

from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.hashers import (
#     check_password, is_password_usable, make_password,
# )


class User(AbstractUser):
    ROLES = (
        ('user', 'user'),
        ('admin', 'admin')
    )
    email = models.EmailField(
        unique=True
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Логин'
    )
    password = models.CharField(_('password'), max_length=128)
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия'
    )

    class Meta:
        abstract = True
