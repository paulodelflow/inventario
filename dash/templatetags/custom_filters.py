from django import template

register = template.Library()

@register.filter
def currency(value):
    """
    Formatea el valor como moneda.
    """
    try:
        value = float(value)
    except (ValueError, TypeError):
        return value
    return "${:,.2f}".format(value)
