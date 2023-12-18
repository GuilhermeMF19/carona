from django import template
from datetime import datetime
from django.utils import timezone
import decimal

register = template.Library()

@register.filter
def is_future_date(datetime_value):
    return datetime_value > timezone.now()

@register.filter
def format_decimal(value):
    return str(value).rstrip('0').rstrip('.')  # Remove zeros e ponto decimal do final
