from django.urls import path
from .views import (
    BalanceReportView,
    MonthlySummaryReportView,
    GeneralSummaryReportView,
)

urlpatterns = [
    path("balance/", BalanceReportView.as_view(), name="balance-report"),
    path("monthly-summary/", MonthlySummaryReportView.as_view(), name="monthly-summary-report"),
    path("general-summary/", GeneralSummaryReportView.as_view(), name="general-summary-report"),
]
