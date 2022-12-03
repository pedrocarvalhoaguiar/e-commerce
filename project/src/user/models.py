from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from src.utility.models import BaseModel
import pathlib
import uuid

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseModel):

    def path_to_profile_image(self, filename):
        extension = pathlib.Path(filename).suffix
        new_filename = str(uuid.uuid4()) + extension
        return f'user/images/{new_filename}'

    email = models.EmailField(_('email address'), unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    last_login = models.DateTimeField(auto_now=True, null=True)
    profile_image = models.ImageField(upload_to=path_to_profile_image, default='user/images/default-profile.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def delete(self):
        self.is_active = False
        super().delete()

    def has_perm(self, perm, obj=None):
        return self.is_admin or self.is_superuser

    def has_module_perms(self, app_label: str) -> bool:
        return True

    def __str__(self):
        return self.email