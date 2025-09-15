from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.transactions.models import Transaction
from apps.core.constants import TransactionTypes
from .serializers import (
    BalanceReportSerializer,
    MonthlySummaryReportSerializer,
    GeneralSummaryReportSerializer,
)


class BalanceReportView(APIView):
    """
    Endpoint: /api/reports/balance/
    Mostra o saldo total (receitas, despesas e saldo final).
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)

        total_income = transactions.filter(
            type=TransactionTypes.INCOME
        ).aggregate(total=Sum("amount"))["total"] or 0

        total_expense = transactions.filter(
            type=TransactionTypes.EXPENSE
        ).aggregate(total=Sum("amount"))["total"] or 0

        balance = total_income - total_expense

        data = {
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": balance,
        }

        serializer = BalanceReportSerializer(data)
        return Response(serializer.data)


class MonthlySummaryReportView(APIView):
    """
    Endpoint: /api/reports/monthly-summary/?year=2025&month=9
    Mostra receitas e despesas do usuário em um mês específico, agrupadas por categoria.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        year = int(request.query_params.get("year"))
        month = int(request.query_params.get("month"))

        transactions = Transaction.objects.filter(
            user=request.user,
            date__year=year,
            date__month=month
        ).values("category__name", "type").annotate(total=Sum("amount"))

        income = []
        expense = []

        for t in transactions:
            entry = {"category": t["category__name"], "total": t["total"]}
            if t["type"] == TransactionTypes.INCOME:
                income.append(entry)
            else:
                expense.append(entry)

        data = {"income": income, "expense": expense}
        serializer = MonthlySummaryReportSerializer(data)
        return Response(serializer.data)


class GeneralSummaryReportView(APIView):
    """
    Endpoint: /api/reports/general-summary/
    Mostra o total de receitas e despesas em TODAS as categorias
    dentro de um ano/mês OU intervalo de datas.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        year = request.query_params.get("year")
        month = request.query_params.get("month")
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        filters = {"user": request.user}

        # 🎯 Prioridade 1 → intervalo de datas
        if start_date and end_date:
            filters["date__range"] = [start_date, end_date]
        # 🎯 Prioridade 2 → ano/mês
        elif year:
            filters["date__year"] = int(year)
            if month:
                filters["date__month"] = int(month)

        transactions = Transaction.objects.filter(**filters)

        income = (
            transactions.filter(type=TransactionTypes.INCOME)
            .values("category__name")
            .annotate(total=Sum("amount"))
            .order_by("category__name")
        )

        expense = (
            transactions.filter(type=TransactionTypes.EXPENSE)
            .values("category__name")
            .annotate(total=Sum("amount"))
            .order_by("category__name")
        )

        data = {
            "year": int(year) if year else None,
            "month": int(month) if month else None,
            "start_date": start_date,
            "end_date": end_date,
            "income": list(income),
            "expense": list(expense),
        }

        serializer = GeneralSummaryReportSerializer(data)
        return Response(serializer.data)
