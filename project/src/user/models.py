from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from src.utility.models import BaseModel

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseModel):

    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def delete(self):
        self.is_active = False
        super().delete()


    def __str__(self):
        return self.email