from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet

# Criamos um router para gerar automaticamente as rotas do CRUD
router = DefaultRouter()
router.register(r"", TransactionViewSet, basename="transaction")

urlpatterns = router.urls
