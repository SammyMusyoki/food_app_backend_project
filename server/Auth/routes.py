from flask_restful import Api
from .Register import  RegisterApi
from .Login import LoginApi

def create_authentication_routes(api: Api):
    api.add_resource(RegisterApi, '/register')
    api.add_resource(LoginApi, '/login')