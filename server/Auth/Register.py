from flask import Response
from flask_restful import Resource
from flask import request, make_response
from Auth.service import create_user, login_user


class RegisterApi(Resource):
    @staticmethod
    def post():
        input_data = request.get_json()
        response, status = create_user(input_data, request)
        return make_response(response, status)