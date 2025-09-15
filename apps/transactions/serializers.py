from rest_framework import serializers
from apps.core.serializers import TimestampMixin
from .models import Transaction

class TransactionSerializer(TimestampMixin, serializers.ModelSerializer):
    

    class Meta:
        model = Transaction
        fields = [
            "id",
            "type",
            "amount",
            "description",
            "date",
            "category",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
