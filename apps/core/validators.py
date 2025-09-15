from django.core.exceptions import ValidationError
from decimal import Decimal
from datetime import date

def validate_positive_decimal(value):
    """
    Valida que o valor decimal é positivo.
    """
    if value <= Decimal("0"):
        raise ValidationError("O valor deve ser maior que zero.")

def validate_date_not_future(value):
    """
    Valida que a data não está no futuro.
    """
    if value > date.today():
        raise ValidationError("A data não pode estar no futuro.")
