import json
import datetime

# Dlango imports
from django.http import HttpResponse, HttpResponseNotFound


def json_class_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    elif hasattr(obj, 'toString'):
        return obj.toString()
    else:
        return obj
    #elif isinstance(obj, ...):
    #    return ...
    #else:
    #    raise TypeError, 'Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj))


class JsonResponse(HttpResponse):
    """
        JSON response
    """
    def __init__(self, content, content_type='application/json', status=None, mimetype=None):
        super(JsonResponse, self).__init__(
            content=json.dumps(content, default=json_class_handler),
            mimetype=mimetype,
            status=status,
            content_type=content_type,
        )


