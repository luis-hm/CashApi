from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .pagination import StandardResultsSetPagination

class BaseViewSet(viewsets.ModelViewSet):
    """
    ViewSet base com configurações comuns para isolar dados por usuário.
    """
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        Filtra queryset apenas para objetos do usuário autenticado.
        """
        return self.queryset.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        """
        Define automaticamente o usuário autenticado no campo 'usuario'.
        """
        serializer.save(usuario=self.request.user)
