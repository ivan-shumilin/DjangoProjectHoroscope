from django import template

register = template.Library()
#  Навешиваем декоратор 
@register.filter(name='split')
def split(value, key=' '):
    return value.split(key)

@register.filter(name='length')
def length(value):
    return len(value)