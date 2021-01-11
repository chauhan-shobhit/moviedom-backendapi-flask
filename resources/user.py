from flask import request
from flask_restful import Resource, Api
from http import HTTPStatus
from models.user import User
from passlib.hash import pbkdf2_sha256
from utils import hash_password
import messages


class UserResource(Resource):

    def post(self):
        user_info = request.get_json()

        user_name = user_info.get('user_name')
        email = user_info.get('email')
        plain_text_password = user_info.get('password')

        if User.find_by_username(user_name):
            return {'message': messages.USERNAME_ALREADY_EXISTS}, HTTPStatus.BAD_REQUEST
        if User.find_by_email(email):
            return {'messages' : messages.EMAIL_ALREADY_EXISTS}
        
        hashed_password = hash_password(plain_text_password)

        new_user = User(
            user_name = user_name,
            email = email,
            password = hashed_password

        ) 

        
        new_user.save()

        return{'message' : messages.USER_CREATION_SUCCESSFUL}, HTTPStatus.CREATED




 
















def hash_password(password):
    return pbkdf2_sha256.hash(password)


def check_password(password, hashed):
    return pbkdf2_sha256.verify(password, hashed)

