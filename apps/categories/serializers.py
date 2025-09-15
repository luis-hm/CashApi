from rest_framework import serializers
from .models import Category
from apps.core.serializers import TimestampMixin

class CategorySerializer(TimestampMixin, serializers.ModelSerializer):
    """
    Serializer para converter objeto Category em JSON e vice-versa.
    """
    class Meta:
        model = Category
        fields = ["id", "name", "color", "created_at", "updated_at"]
