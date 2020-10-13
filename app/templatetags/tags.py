from django import template

register = template.Library()


@register.filter
def to_float(val):
    return float(val)
