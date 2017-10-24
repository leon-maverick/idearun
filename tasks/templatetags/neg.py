from django import template
register = template.Library()

@register.simple_tag
def negate(boolean):
    return (not boolean).__str__()


