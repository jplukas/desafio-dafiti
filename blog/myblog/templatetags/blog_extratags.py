from django import template

register = template.Library()

# Integer division
@register.filter
def intdiv(value, arg):
    return int(value) // arg
