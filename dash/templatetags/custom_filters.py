from django import template
import locale

register = template.Library()
@register.filter
def currency(value):
    locale.setlocale(locale.LC_ALL, '')  # Configura la configuración regional actual del sistema
    return locale.currency(value, grouping=True)
