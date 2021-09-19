from flask import request, make_response, jsonify
from flask.views import MethodView
from src.services import AuthService

class SignupController(MethodView):
    
    def __init__(self) -> None:
        self.auth_service = AuthService()

    def get(self):
        pass
    
    def post(self):
        if request.is_json:
            username = request.json['username']
            password = request.json['password']
            fullname = request.json['fullname']
            return self.auth_service.signup_user(username, password, fullname)
        response = make_response(jsonify({
            "message": "invalid data from body, please send a json format"
        }), 401)
        return response