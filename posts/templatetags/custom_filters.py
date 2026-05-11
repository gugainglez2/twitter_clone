from django import template

register = template.Library()

@register.filter
def replace(value, args):
    """
    Uso: {{ string|replace:"old,new" }}
    Exemplo: {{ "hello world"|replace:"world,there" }} -> "hello there"
    """
    try:
        old, new = args.split(',')
        return value.replace(old, new)
    except ValueError:
        return value