from django import template

import re

register = template.Library()

@register.filter(name='empha')
def empha(value, arg):
    """Embrace the search string with a <font> tag"""
    ivalue = re.compile(re.escape(arg), re.IGNORECASE)
    return ivalue.sub('<font color="red">' + arg + "</font>", value)
