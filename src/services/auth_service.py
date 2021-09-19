from flask import make_response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from src.database import db
from src.models import User
import asyncio, jwt, datetime

class AuthService:
    
    def signin_user(self, username: str, password: str):
        user = User.query.filter_by(username=username).first()
        if user:
            verify_password = check_password_hash(user.password, password)
            if verify_password:
                token: str = jwt.encode({
                    "username": username,
                    "password": password,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
                }, "b'\xfd\xf5\x9cD\xa7<\x13&&\xab/\xbf`b\x1bn'")
                response = make_response(jsonify({
                    "message": f"Hello {user.username}! Welcome back...",
                    "token": token
                }), 201)
                response.headers['Authorization'] = token
                return response
            return make_response(jsonify({
                "message": "Wrong password"
            }), 400)
        return make_response(jsonify({
            "message": "User credentials are incorrect"
        }), 401)
    
    def signup_user(self, username: str, password: str, fullname: str):
        user = User.query.filter_by(username=username).first()
        if not user:
            hash_password = generate_password_hash(password)
            try:
                new_user = User(username, hash_password, fullname)
                db.session.add(new_user)
                db.session.commit()
                token: str = jwt.encode({
                    "username": username,
                    "fullname": fullname,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
                }, "b'\xfd\xf5\x9cD\xa7<\x13&&\xab/\xbf`b\x1bn'")
                response = make_response(jsonify({
                    "message": f"Success! Your user {username} was create",
                    "token": token
                }), 201)
                response.headers['Authorization'] = token
                return response
            except Exception as e:
                return make_response(jsonify({
                    "message": f"{e}"
                }), 401)
        return make_response(jsonify({
            "message": "User exists"
        }), 400)