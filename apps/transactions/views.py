from apps.core.viewsets import BaseViewSet
from apps.core.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(BaseViewSet):
    """
    CRUD de transações financeiras.
    Somente usuários autenticados podem acessar,
    e cada usuário só vê suas próprias transações.
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated, IsOwner]
