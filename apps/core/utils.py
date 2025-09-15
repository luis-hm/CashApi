from datetime import datetime
import pytz
from django.conf import settings

def get_timezone():
    """Obtém o fuso horário da aplicação"""
    return pytz.timezone(settings.TIME_ZONE)

def to_local_datetime(dt):
    """Converte datetime para o fuso horário local"""
    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    return dt.astimezone(get_timezone())

def format_currency(value):
    """Formata valor decimal como moeda (BRL)"""
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
