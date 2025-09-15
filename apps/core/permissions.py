from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Permite acesso apenas ao proprietário do objeto (campo 'usuario').
    """

    def has_object_permission(self, request, view, obj):
        return getattr(obj, "usuario", None) == request.user
