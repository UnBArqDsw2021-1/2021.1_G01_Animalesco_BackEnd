from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return f"{self.email} - {self.username}"