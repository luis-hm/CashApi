# apps/transactions/models.py
from django.db import models
from django.conf import settings
from apps.core.models import BaseModel
from apps.core.validators import validate_positive_decimal, validate_date_not_future
from apps.core.constants import TransactionTypes
from apps.categories.models import Category

class Transaction(BaseModel):
    """
    Representa uma transação financeira (receita ou despesa).
    Cada transação pertence a um usuário e pode estar associada a uma categoria.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transactions"
    )  # Usuário dono da transação

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transactions"
    )  # Categoria vinculada (pode ser nula)

    type = models.CharField(
        max_length=10,
        choices=TransactionTypes.CHOICES
    )  # Tipo: Receita (INCOME) ou Despesa (EXPENSE)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[validate_positive_decimal]
    )  # Valor da transação

    description = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )  # Descrição opcional

    date = models.DateField(
        validators=[validate_date_not_future]
    )  # Data da transação, não pode estar no futuro

    class Meta:
        ordering = ["-date", "-created_at"]  # Mais recentes primeiro

    def __str__(self):
        return f"{self.type} - {self.amount} ({self.user.username})"
