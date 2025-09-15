from rest_framework import serializers

class TimestampMixin(serializers.Serializer):
    """
    Mixin para adicionar campos de timestamp aos serializers.
    """
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
