from flask import config, request, make_response
from flask.json import jsonify
import asyncio, jwt, datetime

class AuthService:
    
    def signin_user(self, username: str, password: str):
        if password == '12345':
            token: str = jwt.encode({
                "username": username,
                "password": password,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
            }, "b'\xfd\xf5\x9cD\xa7<\x13&&\xab/\xbf`b\x1bn'")
            response = make_response(jsonify({
                "username": username,
                "password": password,
                "message": "Sign in an user",
                "token": token
            }), 201)
            response.headers['Authorization'] = token
            return response
        return make_response(jsonify({
            "message": "Wrong password"
        }), 401)