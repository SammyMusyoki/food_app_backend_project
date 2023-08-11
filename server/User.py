from flask import Blueprint, jsonify,request,make_response
from flask_marshmallow import Marshmallow
from models import User,db,Customers,Driver,Admin,SuperAdmin,Favourites
from schemas import *



user = Blueprint("User", __name__)
ma = Marshmallow(user)






@user.route('/')
def index():
    return "User Page"

# CUSTOMERS
@user.route('/customers', methods=['GET'])
def get_all_customers():
    customers = Customers.query.all()
    customer_schema = CustomersSchema(many=True)
    customer_data = customer_schema.dump(customers)
    return jsonify(customer_data)

@user.route('/customers/<int:customer_id>', methods=['GET'])
def get_customers_by_id(customer_id):
    customer = Customers.query.get(customer_id)
    if customer is None:
        return jsonify({'message': 'Customer not found'}), 404
    customer_schema = CustomersSchema()
    customer_data = customer_schema.dump(customer)
    return jsonify(customer_data)
  

@user.route('/customers', methods=['POST'])
def create_customers():
    data = request.get_json()

    customer_schema = CustomersSchema()
    customers = customer_schema.load(data)

    new_customer = Customers(**customers)

    db.session.add(new_customer)
    db.session.commit()

    customer_data = customer_schema.dump(new_customer)
    return jsonify(customer_data), 201
  

@user.route('/customers/<int:customer_id>', methods=['PATCH'])
def update_customer(customer_id):
    data = request.get_json()

    customers = Customers.query.filter_by(customer_id=customer_id).first()
    if not customers:
        return jsonify({'message': "The customer you are looking for is not found"}), 404

    customer_schema = CustomersSchema()
    updated_customer_data = customer_schema.load(data, partial=True)

    for key, value in updated_customer_data.get('customers', {}).items():
        setattr(customers, key, value)

    db.session.commit()
    customer_data = customer_schema.dump(customers)
    return jsonify(customer_data)


@user.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customers = Customers.query.filter_by(customer_id=customer_id).first()
    if not customers:
        return jsonify({'message': 'Customers not found'}), 404

    db.session.delete(customers)
    db.session.commit()

    return jsonify({'message': 'Customer deleted succesfully'}), 204


# DRIVER
        
@user.route('/drivers', methods=['GET'])
def get_all_drivers():
    driver = Driver.query.all()
    driver_schema = DriverSchema(many=True)
    driver_data = driver_schema.dump(driver)
    return jsonify(driver_data)


@user.route('/drivers/<int:driver_id>', methods=['GET'])
def get_driver_by_id(driver_id):
    driver = Driver.query.get(driver_id)
    if driver is None:
        return jsonify({'message': 'Driver not found'}), 404
    driver_schema = DriverSchema()
    driver_data = driver_schema.dump(driver)
    return jsonify(driver_data)


@user.route('/drivers', methods=['POST'])
def create_drivers():
    data = request.get_json()
    driver = DriverSchema().load(data)
    new_driver = Driver(**driver)
    db.session.add(new_driver)
    db.session.commit()
    driver_data = DriverSchema().dump(new_driver)
    return make_response(jsonify(driver_data), 201)

@user.route('/drivers/<int:driver_id>', methods=['PATCH'])
def update_driver(driver_id):
    data = request.get_json()

    driver = Driver.query.filter_by(driver_id=driver_id).first()
    if not driver:
        return jsonify({'message': "The driver you are looking for is not found"}), 404

    driver_schema = DriverSchema()
    updated_driver_data = driver_schema.load(data, partial=True)

    for key, value in updated_driver_data.get('driver', {}).items():
        setattr(driver, key, value)

    db.session.commit()
    driver_data = driver_schema
    
@user.route('/drivers/<int:driver_id>', methods=['DELETE'])
def delete_driver(driver_id):
    driver = Driver.query.filter_by(driver_id=driver_id).first()
    if not driver:
        return jsonify({'message': 'Driver not found'}), 404

    db.session.delete(driver)
    db.session.commit()

    return jsonify({'message': 'Driver deleted succesfully'}), 204

# USER


        
@user.route('/users', methods=['GET'])
def get_all_users():
    user = User.query.all()
    user_schema = UserSchema(many=True)
    user_data = user_schema.dump(user)
    return jsonify(user_data)

@user.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    user_schema = UserSchema()
    user_data = user_schema.dump(user)
    return jsonify(user_data)


@user.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    user_schema = UserSchema()
    user = user_schema.load(data)

    new_user = User(**user)

    db.session.add(new_user)
    db.session.commit()

    user_data = user_schema.dump(new_user)
    return jsonify(user_data), 201

@user.route('/user/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    data = request.get_json()

    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({'message': "The user you are looking for is not found"}), 404

    user_schema = UserSchema()
    updated_user_data = user_schema.load(data, partial=True)

    for key, value in updated_user_data.get('user', {}).items():
        setattr(user, key, value)

    db.session.commit()
    user_data = user_schema
    
@user.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted succesfully'}), 204

# ADMIN

        
@user.route('/admin', methods=['GET'])
def get_all_admin():
    admin = Admin.query.all()
    admin_schema = AdminSchema(many=True)
    admin_data = admin_schema.dump(admin)
    return jsonify(admin_data)


@user.route('/admin/<int:admin_id>', methods=['GET'])
def get_admin_by_id(admin_id):
    admin = Admin.query.get(admin_id)
    if admin is None:
        return jsonify({'message': 'Admin not found'}), 404
    admin_schema = AdminSchema()
    admin_data = admin_schema.dump(admin)
    return jsonify(admin_data)


@user.route('/admin', methods=['POST'])
def create_admin():
    data = request.get_json()

    admin_schema = AdminSchema()
    admin = admin_schema.load(data)

    new_admin = Admin(**admin)

    db.session.add(new_admin)
    db.session.commit()

    admin_data = admin_schema.dump(new_admin)
    return jsonify(admin_data), 201

@user.route('/admin/<int:admin_id>', methods=['DELETE'])
def delete_admin(admin_id):
    admin = Admin.query.filter_by(admin_id=admin_id).first()
    if not admin:
        return jsonify({'message': 'Admin not found'}), 404

    db.session.delete(admin)
    db.session.commit()

    return jsonify({'message': 'admin deleted succesfully'}), 204

# SUPERADMIN
        
@user.route('/superadmin', methods=['GET'])
def get_all_superadmin():
    superadmin = SuperAdmin.query.all()
    superadmin_schema = SuperAdminSchema(many=True)
    superadmin_data = superadmin_schema.dump(superadmin)
    return jsonify(superadmin_data)


@user.route('/superadmin/<int:superadmin_id>', methods=['GET'])
def get_superadmin_by_id(superadmin_id):
    superadmin = SuperAdmin.query.get(superadmin_id)
    if superadmin is None:
        return jsonify({'message': 'SuperAdmin not found'}), 404
    superadmin_schema = SuperAdminSchema()
    superadmin_data = superadmin_schema.dump(superadmin)
    return jsonify(superadmin_data)


@user.route('/superadmin', methods=['POST'])
def create_superadmin():
    data = request.get_json()

    superadmin_schema = SuperAdminSchema()
    superadmin = superadmin_schema.load(data)

    new_superadmin = SuperAdmin(**superadmin)

    db.session.add(new_superadmin)
    db.session.commit()

    superadmin_data = superadmin_schema.dump(new_superadmin)
    return jsonify(superadmin_data), 201

@user.route('/superadmin/<int:superadmin_id>', methods=['DELETE'])
def delete_superadmin(superadmin_id):
    superadmin = SuperAdmin.query.filter_by(superadmin_id=superadmin_id).first()
    if not superadmin:
        return jsonify({'message': 'SuperAdmin not found'}), 404

    db.session.delete(superadmin)
    db.session.commit()

    return jsonify({'message': 'Superadmin deleted succesfully'}), 204

        #   FAVOURITES


@user.route('/favourites', methods=['GET'])
def get_all_favourites():
    favourite = Favourites.query.all()
    favourite_schema = FavouritesSchema(many=True)
    favourite_data = favourite_schema.dump(favourite)
    return jsonify(favourite_data)


@user.route('/favourites', methods=['POST'])
def create_favourites():
    data = request.get_json()
    favourite = FavouritesSchema().load(data)
    new_favourite = Favourites(**favourite)
    db.session.add(new_favourite)
    db.session.commit()
    favourite_data = FavouritesSchema().dump(new_favourite)
    return make_response(jsonify(favourite_data), 201)

@user.route('/favourites/<int:favourite_id>', methods=['DELETE'])
def delete_favourite(favourite_id):
    favourite = Favourites.query.filter_by(favourite_id=favourite_id).first()
    if not favourite:
        return jsonify({'message': 'Favourites not found'}), 404

    db.session.delete(favourite)
    db.session.commit()

    return jsonify({'message': 'Favourites deleted succesfully'}), 204
