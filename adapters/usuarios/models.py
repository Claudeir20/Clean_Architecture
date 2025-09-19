from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UsuarioModel(AbstractBaseUser):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tipo = models.CharField(max_length=20, default='cliente')

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.nome