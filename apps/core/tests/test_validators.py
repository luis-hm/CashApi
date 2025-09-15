from django.core.exceptions import ValidationError
from django.test import TestCase
from datetime import date, timedelta
from decimal import Decimal
from apps.core.validators import validate_positive_decimal, validate_date_not_future

class ValidatorTests(TestCase):

    def test_validate_positive_decimal_ok(self):
        validate_positive_decimal(Decimal("10.00"))  # não deve lançar erro

    def test_validate_positive_decimal_fail(self):
        with self.assertRaises(ValidationError):
            validate_positive_decimal(Decimal("0"))

    def test_validate_date_not_future_ok(self):
        validate_date_not_future(date.today())

    def test_validate_date_not_future_fail(self):
        future = date.today() + timedelta(days=1)
        with self.assertRaises(ValidationError):
            validate_date_not_future(future)
