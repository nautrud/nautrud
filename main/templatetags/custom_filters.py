from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """
    Split a string by the given delimiter
    Usage: {{ value|split:"/" }}
    """
    return value.split(arg)

@register.filter
def strip(value):
    """
    Strip whitespace from a string
    Usage: {{ value|strip }}
    """
    return value.strip()

@register.filter
def split_tags(value):
    """
    Split tags string by comma and strip whitespace
    Usage: {{ value|split_tags }}
    """
    if not value:
        return []
    return [tag.strip() for tag in value.split(',') if tag.strip()] 