from rest_framework import serializers

class BalanceReportSerializer(serializers.Serializer):
    """
    Define o formato de saída do relatório de saldo.
    """
    total_income = serializers.DecimalField(max_digits=12, decimal_places=2)
    total_expense = serializers.DecimalField(max_digits=12, decimal_places=2)
    balance = serializers.DecimalField(max_digits=12, decimal_places=2)


class CategorySummarySerializer(serializers.Serializer):
    """
    Usado dentro do resumo mensal para mostrar valores por categoria.
    """
    category = serializers.CharField()
    total = serializers.DecimalField(max_digits=12, decimal_places=2)


class MonthlySummaryReportSerializer(serializers.Serializer):
    """
    Define o formato de saída do relatório mensal.
    """
    income = CategorySummarySerializer(many=True)
    expense = CategorySummarySerializer(many=True)


class CategoryTotalSerializer(serializers.Serializer):
    category__name = serializers.CharField()
    total = serializers.DecimalField(max_digits=12, decimal_places=2)


class GeneralSummaryReportSerializer(serializers.Serializer):
    """
    Mostra o resumo geral de receitas e despesas por categoria.
    """
    year = serializers.IntegerField(required=False, allow_null=True)
    month = serializers.IntegerField(required=False, allow_null=True)
    start_date = serializers.DateField(required=False, allow_null=True)
    end_date = serializers.DateField(required=False, allow_null=True)
    income = CategoryTotalSerializer(many=True)
    expense = CategoryTotalSerializer(many=True)