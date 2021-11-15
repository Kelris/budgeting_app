from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('Email address'), unique=True)

    def __str__(self):
        return f"{self.id} - {self.username} {self.full_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
