from django.db import models
from django.conf import settings
from apps.core.models import BaseModel
from apps.core.constants import Colors

class Category(BaseModel):
    """
    Representa uma categoria de transações financeiras.
    Cada usuário pode ter suas próprias categorias.
    """
    name = models.CharField(max_length=100)  # Nome da categoria
    color = models.CharField(
        max_length=7,
        choices=Colors.CHOICES,
        default=Colors.PRIMARY
    )  # Cor usada em relatórios
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )  # Usuário dono da categoria

    class Meta:
        unique_together = ("name", "user")  # Impede nomes duplicados por usuário
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.user.username})"
