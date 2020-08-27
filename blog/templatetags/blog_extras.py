from django import template

register = template.Library()

@register.filter
def concat_header(value, arg):
    return str(value) + str(arg)