from flask import session, Response
from functools import wraps
import json

def auth_required(func):
    @wraps(func)
    def _func(*args, **kwargs):
        if not 'uid' in session:
            return 'Authorization Required', 403
        else:
            return func(*args, **kwargs)
    return _func

def tojson(func):
    @wraps(func)
    def _func(*args, **kwargs):
        rt = func(*args, **kwargs)
        try:
            return Response(json.dumps(rt), mimetype="application/json")
        except:
            return rt
    return _func
