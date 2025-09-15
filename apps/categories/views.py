from apps.core.viewsets import BaseViewSet
from apps.core.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(BaseViewSet):
    """
    CRUD de categorias.
    Somente usuários autenticados podem acessar,
    e cada usuário só vê suas próprias categorias.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsOwner]
