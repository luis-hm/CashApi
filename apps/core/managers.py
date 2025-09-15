from django.db import models

class ActiveManager(models.Manager):
    """
    Manager para retornar apenas objetos ativos.
    Útil para implementar soft delete no futuro.
    """
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
