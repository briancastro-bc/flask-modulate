from flask import request, make_response
from flask.views import MethodView
from src.services import AuthService

class LogInController(MethodView):
    
    def __init__(self) -> None:
        super().__init__()
        self.auth_service = AuthService()
    
    def get(self):
        pass
    
    def post(self):
        if request.is_json:
            username = request.json['username']
            password = request.json['password']
            return self.auth_service.signin_user(username, password)
        response = make_response({
            "message": "The request is invalid, please send a JSON"
        }, 400)
        return response