from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    """
    Manipulador personalizado de exceções com logging.
    """
    response = exception_handler(exc, context)

    if response is not None:
        status_code = response.status_code
        message = "Ocorreu um erro"

        if status_code == status.HTTP_400_BAD_REQUEST:
            message = "Erro de validação"
        elif status_code == status.HTTP_403_FORBIDDEN:
            message = "Sem permissão para acessar este recurso"
        elif status_code >= 500:
            message = "Erro interno no servidor"

        # Loga a exceção
        logger.error(f"Erro na API: {exc}", extra={
            "view": str(context.get("view")),
            "request": str(context.get("request")),
            "exception": str(exc),
        })

        response.data = {
            "error": True,
            "message": message,
            "details": response.data,
        }

    return response
