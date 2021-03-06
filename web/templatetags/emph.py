from django import template

import re

register = template.Library()

@register.filter(name='empha')
def empha(value, arg, colour='red'):
    """Embrace the search string with a <font> tag"""
    ivalue = re.compile(re.escape(arg), re.IGNORECASE)
    return ivalue.sub('<font color="' + colour  + '">' + arg + "</font>", value)
