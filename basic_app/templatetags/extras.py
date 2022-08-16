from django import template

register = template.Library()

@register.filter(namde="cut")
def cut(value,arg):
    """
    This cut out all value of args from string
    """
    return value.replace(arg,"")


# register.filter('cut',cut)
