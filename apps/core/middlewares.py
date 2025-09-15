import uuid
import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(MiddlewareMixin):
    """
    Middleware para adicionar ID de requisição e logar informações básicas.
    """

    def process_request(self, request):
        request.id = str(uuid.uuid4())
        request.META["HTTP_X_REQUEST_ID"] = request.id

        logger.info(
            f"Requisição iniciada: {request.method} {request.path}",
            extra={
                "request_id": request.id,
                "method": request.method,
                "path": request.path,
                "user": getattr(request.user, "id", None),
            },
        )

    def process_response(self, request, response):
        response["X-Request-ID"] = getattr(request, "id", "unknown")

        logger.info(
            f"Requisição concluída: {response.status_code}",
            extra={
                "request_id": getattr(request, "id", "unknown"),
                "status_code": response.status_code,
            },
        )

        return response
