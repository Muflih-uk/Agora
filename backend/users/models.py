from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
# That is App User Model
class AppUser(AbstractUser):
    username = models.CharField(max_length=50, unique= True)
    email = models.EmailField(_('email address'),unique= True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "{}".format(self.email)