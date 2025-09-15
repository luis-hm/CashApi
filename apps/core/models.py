from django.db import models
import uuid

class BaseModel(models.Model):
    """
    Modelo base com campos comuns para todos os modelos.
    Inclui UUID como chave primária e timestamps.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
