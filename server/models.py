from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from datetime import datetime
from sqlalchemy.orm import validates
from schemas import *
from werkzeug.security import generate_password_hash, check_password_hash

import jwt


db = SQLAlchemy()


class Owner(db.Model):
    __tablename__ = 'owner'
    owner_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    image = db.Column(db.String)

    locations = db.relationship('Location', backref='owner')
    restaurants= db.relationship('Restaurant', back_populates='owner')
    
   
class Location(db.Model):
    __tablename__ = 'location'
    location_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, ForeignKey('owner.owner_id'))
    name = db.Column(db.String)
    delivery_fee = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, ForeignKey('restaurant.restaurant_id'))
    restaurant = db.relationship('Restaurant', backref='location')


class Order(db.Model):
    __tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, ForeignKey('menu.menu_id'))
    total_price = db.Column(db.Integer)
    order_date_and_time = db.Column(db.DateTime)
    address = db.Column(db.String)
    payment_method = db.Column(db.String)

    deliveries = db.relationship('Deliveries', backref='order')


class Driver(db.Model):
    __tablename__ = 'driver'
    driver_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    phone_number = db.Column(db.String)
    image = db.Column(db.String)
    current_location = db.Column(db.String)

    deliveries = db.relationship('Deliveries', backref='driver')


class Deliveries(db.Model):
    __tablename__ = 'deliveries'
    delivery_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, ForeignKey('order.order_id')) 
    driver_id = db.Column(db.Integer, ForeignKey('driver.driver_id'))
    delivery_date_and_time = db.Column(db.DateTime)
    dispatch = db.Column(db.Boolean, default=False)
    delivered = db.Column(db.Boolean, default=False)  
  
    
class Payment(db.Model):
    __tablename__ = 'payment'
    payment_id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, ForeignKey('restaurant.restaurant_id'))
    payment_type = db.Column(db.String)
    payment_amount = db.Column(db.Integer)
    payment_date_and_time = db.Column(db.Time)
    payment_status = db.Column(db.String)

class Customers(db.Model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user_name = db.Column(db.String)
    password = db.Column(db.String)
    phone_number = db.Column(db.String)
    image = db.Column(db.String)

    customerReviews = db.relationship('CustomerReviews', backref='customer')
    user = db.relationship('User', backref='customer', uselist=False)

class CustomerReviews(db.Model):
    __tablename__ = 'customerReviews'
    customerReview_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, ForeignKey('customers.customer_id'))
    rating = db.Column(db.Integer)
    review_comment = db.Column(db.String)
    review_date = db.Column(db.DateTime)
    
class RestaurantReviews(db.Model):
    __tablename__ = 'restaurantReviews'
    restaurantReview_id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, ForeignKey('restaurant.restaurant_id'))
    rating = db.Column(db.Integer)
    review_comment = db.Column(db.String)
    review_date = db.Column(db.DateTime)
    
class MenuReviews(db.Model):
    __tablename__ = 'menuReviews'
    restaurantReview_id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, ForeignKey('menu.menu_id'))
    rating = db.Column(db.Integer)
    review_comment = db.Column(db.String)
    review_date = db.Column(db.DateTime)

class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    restaurant_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer,ForeignKey('owner.owner_id'))
    restaurant_name = db.Column(db.String)
    contact_number = db.Column(db.String)
    opening_hours = db.Column(db.Time)
    closing_hours = db.Column(db.Time)
    image = db.Column(db.String)
    payment_method = db.Column(db.String)
    
   
    menus = db.relationship('Menu', backref='restaurant')
    owner = db.relationship('Owner', back_populates='restaurants')
  



class Menu(db.Model):
    __tablename__ = 'menu'
    menu_id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, ForeignKey('restaurant.restaurant_id'))
    menu_name = db.Column(db.String)
    description = db.Column(db.String)
    prices = db.Column(db.Integer)
    description = db.Column(db.String)
    image = db.Column(db.String)
    
    orders = db.relationship("Order", backref = "menu")
  

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    confirm_password = db.Column(db.String)
    type = db.Column(db.Boolean, default=False)  
    blocked = db.Column(db.String)
    activity = db.Column(db.String)
    
    

    def __init__(self, **kwargs):
        self.user_name = kwargs.get('user_name')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')

    def __rep__(self):
        return "<User {}>".format(self.user_name)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)



class Favourites(db.Model):
    __tablename__ ='favourite'
    favourite_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.user_id'))
    menu_id = db.Column(db.Integer, ForeignKey('menu.menu_id'))

class Admin(db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, ForeignKey('customers.customer_id'))
    restaurant_id = db.Column(db.Integer, ForeignKey('restaurant.restaurant_id'))
    owner_id = db.Column(db.Integer, ForeignKey('owner.owner_id'))
    name = db.Column(db.String)
    password = db.Column(db.String)
    image = db.Column(db.String)
    
class SuperAdmin(db.Model):
    __tablename__ = 'superadmin'
    superadmin_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, ForeignKey('customers.customer_id'))
    restaurant_id = db.Column(db.Integer, ForeignKey('restaurant.restaurant_id'))
    owner_id = db.Column(db.Integer, ForeignKey('owner.owner_id'))
    name = db.Column(db.String)
    password = db.Column(db.String)
    image = db.Column(db.String)
    
    @validates("password")
    def validate_password(self, key, password):
        if password and len(password) > 100:
            raise ValueError('User password is not valid, please try again')
        return password

   