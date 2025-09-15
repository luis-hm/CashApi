from django.test import TestCase
from datetime import datetime
import pytz
from apps.core.utils import to_local_datetime, format_currency, get_timezone

class UtilsTests(TestCase):

    def test_get_timezone(self):
        tz = get_timezone()
        self.assertTrue("America" in str(tz) or "UTC" in str(tz))

    def test_to_local_datetime_naive(self):
        dt = datetime.utcnow()
        local_dt = to_local_datetime(dt)
        self.assertIsNotNone(local_dt.tzinfo)

    def test_format_currency(self):
        formatted = format_currency(1234.56)
        self.assertEqual(formatted, "R$ 1.234,56")
