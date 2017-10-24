from django import template

register = template.Library()

@register.simple_tag
def negate(boolean):
	print("hereee"+ boolean)
    return (not boolean).__str__()


