import json
import jwt
import datetime
from models import db
from os import environ
from models import User
from utils.common import generate_response
from schemas import (
    CreateLoginInputSchema,
    CreateSignupInputSchema, 
)
from utils.http_code import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

def create_user(request, input_data):
    create_validation_schema = CreateSignupInputSchema()
    errors = create_validation_schema.validate(input_data)

    if errors:
        return generate_response(message=errors)
    check_username_exists = User.query.filter_by(
        user_name = input_data.get('user_name')
    ).first()

    check_email_exist = User.query.filter_by(
        email = input_data.get('email')
    ).first()

    if check_username_exists:
        return generate_response(message='Username already exists', status=HTTP_400_BAD_REQUEST)
    elif check_email_exist:
        return generate_response(message='Email already exists', status=HTTP_400_BAD_REQUEST)
    
    new_user = User(**input_data)
    new_user.hash_password()
    db.session.add(new_user)
    db.session.commit()

    del input_data['password']
    return generate_response(message='User created successfully', status=HTTP_201_CREATED, data=input_data)

def login_user(request, input_data):
    login_validation_schema = CreateLoginInputSchema()
    errors = login_validation_schema.validate(input_data)

    get_user = User.query.filter_by(email=input_data['email']).first()
    if get_user is None:
        return generate_response(message='User not found', status=HTTP_400_BAD_REQUEST)
    if get_user.check_password(input_data['password']):
        token = jwt.encode(
            {
                'user_id': get_user.id,
                'email' : get_user.email,
                'username' : get_user.username,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)
            },
            environ.get('SECRET_KEY'),
            algorithm='HS256'
        )
        input_data["token"] = token
        return generate_response(
            message='User logged in successfully',
            status=HTTP_201_CREATED,
            data=input_data
        )
    else:
        return generate_response(message='Invalid password', status=HTTP_400_BAD_REQUEST)