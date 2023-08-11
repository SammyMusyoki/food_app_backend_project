#app.py
from flask import Flask, request, jsonify,Blueprint
from flask_jwt_extended import JWTManager,create_access_token
from functools import wraps
import uuid
# from flask_sqlalchemy import SQLAlchemy
from models import db,User,Owner,Customers,Driver,Admin,SuperAdmin
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
from schemas import *



app = Flask(__name__)
main2=Blueprint("main2", __name__)

jwt=JWTManager(app)

migrate = Migrate(app, db)
ma = Marshmallow(app)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'user_name', 'email', 'password','confirm_password', 'type', 'blocked', 'activity')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

    
from datetime import timedelta

@main2.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        # Generate access token with a 1-minute expiration
        expires = timedelta(hours=3)
        token = create_access_token(identity=email, expires_delta=expires)
        return jsonify({"token": token})
    else:
        return jsonify({'message': 'Invalid email or password'}), 401


@main2.route("/register", methods =["POST"])
def create_account():
    user_name = request.json["user_name"]
    email = request.json["email"]
    password = request.json["password"]
    type = request.json["type"]
    confirm_password = request.json["confirm_password"]
    blocked = request.json["blocked"]
    activity = request.json["activity"]
    
   

    user_exists = User.query.filter_by(user_name=user_name, type=type).first()

    if user_exists:
        return jsonify({"error": "Username already exists "})
    else:
        hashed_password= generate_password_hash(password)
        new_user = User(user_name=user_name,email=email, password=hashed_password,type=type,blocked=blocked,activity=activity,confirm_password=confirm_password)

        db.session.add(new_user)
        db.session.commit()


        # access_token = create_access_token(identity=new_user.id)
        access_token = create_access_token(identity={'user_id': new_user.user_id, 'type': type})

        return jsonify({
        "user_id": new_user.user_id,
        "user_name":user_name,
        "email":email,
        "type": type,
        "access_token": access_token,
        "password": password,
        "confirm_password":confirm_password,
        "blocked":blocked,
        "activity":activity
        
        

    })
@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        email = data["email"]
        password = data['password']
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                token = create_access_token(identity=(email))
                return jsonify({"token": token})
            else:
                return jsonify(response="wrong password"),401

        else :
            return jsonify(result="invalid Email"), 401    

# OWNERS AUTHENTICATION

@main2.route('/owner/register', methods=['POST'])
def register_owner():
    data = request.get_json()

    name = data['name']
    email = data['email']
    password = data['password']
    image = data.get('image')  

    owner_exists = Owner.query.filter_by(email=email).first()
    if owner_exists:
        return jsonify({"error": "Email already exists"})

    hashed_password = generate_password_hash(password)
    new_owner = Owner(name=name, email=email, password=hashed_password, image=image)

    db.session.add(new_owner)
    db.session.commit()

    access_token = create_access_token(identity={'owner_id': new_owner.owner_id})

    return jsonify({
        "owner_id": new_owner.owner_id,
        "name": name,
        "email": email,
        "image": image,
        "access_token": access_token
    }), 201

@main2.route('/owner/login', methods=['POST'])
def login_owner():
    data = request.get_json()

    email = data['email']
    password = data['password']

    owner = Owner.query.filter_by(email=email).first()

    if owner:
        if check_password_hash(owner.password, password):
            access_token = create_access_token(identity={'owner_id': owner.owner_id})
            return jsonify({"token": access_token}), 200
        else:
            return jsonify({'message': 'Wrong password'}), 401
    else:
        return jsonify({'message': 'Invalid email'}), 401

# customer authentication

@main2.route('/customers/register', methods=['POST'])
def register_customer():
    data = request.get_json()

    user_name = data['user_name']
    password = data['password']
    phone_number = data['phone_number']
    image = data.get('image')  

 
    customer_exists = Customers.query.filter_by(user_name=user_name).first()
    if customer_exists:
        return jsonify({"error": "Username already exists"})

    hashed_password = generate_password_hash(password)
    new_customer = Customers(user_name=user_name, password=hashed_password, phone_number=phone_number, image=image)

    db.session.add(new_customer)
    db.session.commit()

    access_token = create_access_token(identity={'customer_id': new_customer.customer_id})

    return jsonify({
        "customer_id": new_customer.customer_id,
        "user_name": user_name,
        "phone_number": phone_number,
        "image": image,
        "access_token": access_token
    }), 201

@main2.route('/customers/login', methods=['POST'])
def login_customer():
    data = request.get_json()

    user_name = data['user_name']
    password = data['password']

    customer = Customers.query.filter_by(user_name=user_name).first()

    if customer:
        if check_password_hash(customer.password, password):
            access_token = create_access_token(identity={'customer_id': customer.customer_id})
            return jsonify({"token": access_token}), 200
        else:
            return jsonify({'message': 'Wrong password'}), 401
    else:
        return jsonify({'message': 'Invalid user name'}), 401


# drivers authentication login and register

@main2.route('/driver/register', methods=['POST'])
def register_driver():
    data = request.get_json()

    name = data['name']
    email = data['email']
    password = data['password']
    phone_number = data['phone_number']
    image = data.get('image') 
    current_location = data.get('current_location')  

    driver_exists = Driver.query.filter_by(email=email).first()
    if driver_exists:
        return jsonify({"error": "Email already exists"})

    hashed_password = generate_password_hash(password)
    new_driver = Driver(name=name, email=email, password=hashed_password, phone_number=phone_number,
                        image=image, current_location=current_location)

    db.session.add(new_driver)
    db.session.commit()

    access_token = create_access_token(identity={'driver_id': new_driver.driver_id})

    return jsonify({
        "driver_id": new_driver.driver_id,
        "name": name,
        "email": email,
        "phone_number": phone_number,
        "image": image,
        "current_location": current_location,
        "access_token": access_token
    }), 201

@main2.route('/driver/login', methods=['POST'])
def login_driver():
    data = request.get_json()

    email = data['email']
    password = data['password']

    driver = Driver.query.filter_by(email=email).first()

    if driver:
        if check_password_hash(driver.password, password):
            access_token = create_access_token(identity={'driver_id': driver.driver_id})
            return jsonify({"token": access_token}), 200
        else:
            return jsonify({'message': 'Wrong password'}), 401
    else:
        return jsonify({'message': 'Invalid email'}), 401

    
    
# admin
@main2.route('/admin/register', methods=['POST'])
def register_admin():
    data = request.get_json()

    name = data['name']
    password = data['password']
    image = data.get('image')  
    customer_id = data.get('customer_id')  
    restaurant_id = data.get('restaurant_id') 
    owner_id = data.get('owner_id')  

    admin_exists = Admin.query.filter_by(name=name).first()
    if admin_exists:
        return jsonify({"error": "Admin name already exists"})

    hashed_password = generate_password_hash(password)
    new_admin = Admin(name=name, password=hashed_password, image=image,
                      customer_id=customer_id, restaurant_id=restaurant_id, owner_id=owner_id)

    db.session.add(new_admin)
    db.session.commit()

    access_token = create_access_token(identity={'admin_id': new_admin.admin_id})

    return jsonify({
        "admin_id": new_admin.admin_id,
        "name": name,
        "image": image,
        "customer_id": customer_id,
        "restaurant_id": restaurant_id,
        "owner_id": owner_id,
        "access_token": access_token
    }), 201

@main2.route('/admin/login', methods=['POST'])
def login_admin():
    data = request.get_json()

    name = data['name']
    password = data['password']

    admin = Admin.query.filter_by(name=name).first()

    if admin:
        if check_password_hash(admin.password, password):
            access_token = create_access_token(identity={'admin_id': admin.admin_id})
            return jsonify({"token": access_token}), 200
        else:
            return jsonify({'message': 'Wrong password'}), 401
    else:
        return jsonify({'message': 'Invalid name'}), 401


# superadmin

@main2.route('/superadmin/register', methods=['POST'])
def register_superadmin():
    data = request.get_json()

    name = data['name']
    password = data['password']
    image = data.get('image') 
    customer_id = data.get('customer_id')  
    restaurant_id = data.get('restaurant_id')  
    owner_id = data.get('owner_id')

    superadmin_exists = SuperAdmin.query.filter_by(name=name).first()
    if superadmin_exists:
        return jsonify({"error": "SuperAdmin name already exists"})

    hashed_password = generate_password_hash(password)
    new_superadmin = SuperAdmin(name=name, password=hashed_password, image=image,
                                customer_id=customer_id, restaurant_id=restaurant_id, owner_id=owner_id)

    db.session.add(new_superadmin)
    db.session.commit()

    access_token = create_access_token(identity={'superadmin_id': new_superadmin.superadmin_id})

    return jsonify({
        "superadmin_id": new_superadmin.superadmin_id,
        "name": name,
        "image": image,
        "customer_id": customer_id,
        "restaurant_id": restaurant_id,
        "owner_id": owner_id,
        "access_token": access_token
    }), 201

@main2.route('/superadmin/login', methods=['POST'])
def login_superadmin():
    data = request.get_json()

    name = data['name']
    password = data['password']

    superadmin = SuperAdmin.query.filter_by(name=name).first()

    if superadmin:
        if check_password_hash(superadmin.password, password):
            access_token = create_access_token(identity={'superadmin_id': superadmin.superadmin_id})
            return jsonify({"token": access_token}), 200
        else:
            return jsonify({'message': 'Wrong password'}), 401
    else:
        return jsonify({'message': 'Invalid name'}), 401