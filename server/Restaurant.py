from flask import Blueprint, jsonify,Flask,request,make_response
from datetime import datetime
from flask_marshmallow import Marshmallow
from models import Restaurant,db,Menu,Order,Payment

from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

from schemas import *

restaurants = Blueprint("restaurants", __name__)
ma = Marshmallow()



app = Flask(__name__)
ma.init_app(app)
jwt = JWTManager(app)

@restaurants.route('/')
def index():
    return "This is the Products page"

# RESTAURANTS
# get all restaurant route
@restaurants.route('/restaurants', methods=['GET'])
def get_all_restaurants():
    restaurants_list = Restaurant.query.all()
    restaurant_schema = RestaurantSchema(many=True)
    restaurant_data = restaurant_schema.dump(restaurants_list)  
    return jsonify(restaurant_data)
#   get restaurant by id route
@restaurants.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.filter_by(restaurant_id=restaurant_id).first()
    if restaurant is None:
        return jsonify({'message': 'Restaurant is not found'}), 404

    restaurant_schema = RestaurantSchema()
    restaurant_data = restaurant_schema.dump(restaurant)
    return jsonify(restaurant_data)
#   creating  A new restaurant route
@restaurants.route('/restaurants', methods=['POST'])
def create_restauarants():
    data = request.get_json()
    restaurant = RestaurantSchema().load(data)
    new_restaurant = Restaurant(**restaurant)
    db.session.add(new_restaurant)
    db.session.commit()
    restaurant_data = RestaurantSchema().dump(new_restaurant)
    return make_response(jsonify(restaurant_data), 201)

# updating some details of the restaurant route
@restaurants.route('/restaurants/<int:restaurant_id>', methods=['PATCH'])
def update_restaurant_details(restaurant_id):
    restaurant = Restaurant.query.filter_by(restaurant_id = restaurant_id).first()
    data = request.get_json()
    restaurants = RestaurantSchema().load(data)
    for field, value in restaurants.items():
        setattr(restaurant, field, value)
    db.session.add(restaurant)
    db.session.commit() 

    restaurant_data = RestaurantSchema().dump(restaurant)
    return make_response(jsonify(restaurant_data))

# delete route to delete a restaurant
@restaurants.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.filter_by(restaurant_id=restaurant_id).first()
    if not restaurant:
        return jsonify({'message': 'Restaurant not found'}), 404

    db.session.delete(restaurant)
    db.session.commit()

    return jsonify({'message': 'Restaurant deleted succesfully'}), 204

# MENUS

        
@restaurants.route('/menus', methods=['GET'])
def get_all_menus():
    menu_list = Menu.query.all()
    menu_schema = MenuSchema(many=True)
    menu_data = menu_schema.dump(menu_list)  
    return jsonify(menu_data)


@restaurants.route('/menus/<int:menu_id>', methods=['GET'])
def get_menu(menu_id):
    menu = Menu.query.filter_by(menu_id=menu_id).first()
    if menu is None:
        return jsonify({'message': 'Menu is not found'}), 404

    menu_schema = MenuSchema()
    menu_data = menu_schema.dump(menu)
    return jsonify(menu_data)

@restaurants.route('/menus', methods=['POST'])
def create_menus():
    data = request.get_json()
    menu = MenuSchema().load(data)
    new_menu = Menu(**menu)
    db.session.add(new_menu)
    db.session.commit()
    menu_data = MenuSchema().dump(new_menu)
    return make_response(jsonify(menu_data), 201)


@restaurants.route('/menus/<int:menu_id>', methods=['PATCH'])
def update_menu_details(menu_id):
    menu = Menu.query.filter_by(menu_id = menu_id).first()
    data = request.get_json()
    menus = MenuSchema().load(data)
    for field, value in menus.items():
        setattr(menu, field, value)
    db.session.add(menu)
    db.session.commit() 

    menu_data = MenuSchema().dump(menu)
    return make_response(jsonify(menu_data))



@restaurants.route('/menus/<int:menu_id>', methods=['DELETE'])
def delete_menu(menu_id):
    menu = Menu.query.filter_by(menu_id=menu_id).first()
    if not menu:
        return jsonify({'message': 'Menu not found'}), 404

    db.session.delete(menu)
    db.session.commit()

    return jsonify({'message': 'Menu deleted succesfully'}), 204


# ORDERS

@restaurants.route('/orders', methods=['GET'])
def get_all_orders():
    order_list = Order.query.all()
    order_schema = OrderSchema(many=True)
    order_data = order_schema.dump(order_list)  
    return jsonify(order_data)


@restaurants.route('/orders/<int:order_id>', methods=['GET'])
def get_orders(order_id):
    order = Order.query.filter_by(order_id=order_id).first()
    if order is None:
        return jsonify({'message': 'Orders are not found'}), 404

    order_schema = OrderSchema()
    order_data = order_schema.dump(order)
    return jsonify(order_data)


@restaurants.route('/orders', methods=['POST'])
def create_orders():
    data = request.get_json()
    order = OrderSchema().load(data)
    new_order = Order(**order)
    db.session.add(new_order)
    db.session.commit()
    order_data = OrderSchema().dump(new_order)
    return make_response(jsonify(order_data), 201)


@restaurants.route('/viewing/<int:order_id>', methods=['PATCH'])
def update_order_details(order_id):
    order = Order.query.filter_by(order_id = order_id).first()
    data = request.get_json()
    orders = OrderSchema().load(data)
    for field, value in orders.items():
        setattr(order, field, value)
    db.session.add(order)
    db.session.commit() 

    orders_data = OrderSchema().dump(order)
    return make_response(jsonify(orders_data))



@restaurants.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.filter_by(order_id=order_id).first()
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    db.session.delete(order)
    db.session.commit()

    return jsonify({'message': 'Order deleted succesfully'}), 204

# PAYMENT

        
@restaurants.route('/payment', methods=['GET'])
def get_all_payments():
    payment_list = Payment.query.all()
    payment_schema = PaymentSchema(many=True)
    payment_data = payment_schema.dump(payment_list)  
    return jsonify(payment_data)


@restaurants.route('/payment/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    payment = Payment.query.filter_by(payment_id=payment_id).first()
    if payment is None:
        return jsonify({'message': 'Payments are not found'}), 404

    payment_schema = PaymentSchema()
    payment_data = payment_schema.dump(payment)
    return jsonify(payment_data)

@restaurants.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json()
    payment = PaymentSchema().load(data)
    new_payment = Payment(**payment)
    db.session.add(new_payment)
    db.session.commit()
    payment_data = PaymentSchema().dump(new_payment)
    return make_response(jsonify(payment_data), 201)


@restaurants.route('/payment/<int:payment_id>', methods=['PATCH'])
def update_payment_details(payment_id):
    payment = Payment.query.filter_by(payment_id = payment_id).first()
    data = request.get_json()
    payments = PaymentSchema().load(data)
    for field, value in payments.items():
        setattr(payment, field, value)
    db.session.add(payment)
    db.session.commit() 

    payments_data = PaymentSchema().dump(payment)
    return make_response(jsonify(payments_data))



@restaurants.route('/payment/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    payment = Payment.query.filter_by(payment_id=payment_id).first()
    if not payment:
        return jsonify({'message': 'Payment not found'}), 404

    db.session.delete(payment)
    db.session.commit()

    return jsonify({'message': 'Payment deleted succesfully'}), 204



restaurant_schema = RestaurantSchema()
restaurants_schema = RestaurantSchema(many=True)

@restaurants.route('/search', methods=['GET'])
def search_restaurants():
    query_params = request.args.to_dict()

    filtered_query = Restaurant.query

    if 'q' in query_params:
        filtered_query = filtered_query.filter(Restaurant.restaurant_name.ilike(f"%{query_params['q']}%"))

    if 'rating' in query_params:
        filtered_query = filtered_query.filter(Restaurant.rating >= float(query_params['rating']))

    search_results = filtered_query.all()

    # Serializing the results using the schema
    serialized_results = restaurants_schema.dump(search_results)

    return jsonify(serialized_results)





















        


  