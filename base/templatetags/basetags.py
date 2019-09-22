from datetime import datetime

from django import template

register = template.Library()


@register.filter()
def price_format(value):
    return "{} تومان".format(value)

@register.simple_tag()
def get_time(string_format):
    return datetime.now().strftime(string_format)
