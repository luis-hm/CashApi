# apps/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Modelo customizado de usuário.
    - Usa BigAutoField (padrão) como ID primário
    - Possui campo 'email' único como identificador
    """
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # ainda precisamos do username, mas login será por email

    def __str__(self):
        return self.email
