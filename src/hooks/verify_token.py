from flask import request, make_response, jsonify
from functools import wraps
import jwt

def verify_token(func):
    @wraps(func)
    def hook(*args, **kwargs):
        token = request.headers.get('Authorization', type=str)
        try:
            data = jwt.decode(token, "b'\xfd\xf5\x9cD\xa7<\x13&&\xab/\xbf`b\x1bn'", algorithms=['HS256'])       
            print(data)
        except jwt.InvalidTokenError as e:
            return make_response(jsonify({
                "message": f"The token is missing or invalid. Error: {e}"
            }), 401)
        except jwt.ExpiredSignatureError as e:
            return make_response(jsonify({
                "message": f"The token expired. Error: {e}"
            }), 400)
        return func(*args, **kwargs)
    return hook