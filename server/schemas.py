from marshmallow import Schema, fields, validate
class OwnerSchema(Schema):
    owner_id = fields.Integer()
    name = fields.String()
    email = fields.String()
    password = fields.String()
    image = fields.String()

class LocationSchema(Schema):
    location_id = fields.Integer()
    owner_id = fields.Integer()
    name = fields.String()
    delivery_fee = fields.String()

class OrderSchema(Schema):
    order_id = fields.Integer()
    menu_id = fields.Integer(dump_only=True)
    total_price = fields.Integer()
    order_date_and_time = fields.DateTime()
    address = fields.String()
    payment_method = fields.String()


class DriverSchema(Schema):
    driver_id = fields.Integer()
    name = fields.String()
    email = fields.String()
    password = fields.String()
    phone_number = fields.String()
    image = fields.String()
    current_location = fields.String()


class DeliveriesSchema(Schema):
    delivery_id = fields.Integer()
    order_id = fields.Integer()
    driver_id = fields.Integer()
    delivery_date_and_time = fields.DateTime()
    dispatch = fields.Boolean()
    delivered = fields.Boolean()

class PaymentSchema(Schema):
    payment_id = fields.Integer()
    restaurant_id = fields.Integer()
    payment_type = fields.String()
    payment_amount = fields.Integer()
    payment_date_and_time = fields.DateTime()
    payment_status = fields.String()

class CustomersSchema(Schema):
    customer_id = fields.Integer()
    user_name = fields.String()
    password = fields.String()
    phone_number = fields.String()
    image = fields.String()

class CustomerReviewsSchema(Schema):
    customerReview_id = fields.Integer()
    customer_id = fields.Integer()
    rating = fields.Integer()
    review_comment = fields.String()
    review_date = fields.DateTime()

class RestaurantReviewsSchema(Schema):
    restaurantReview_id = fields.Integer()
    restaurant_id = fields.Integer()
    rating = fields.Integer()
    review_comment = fields.String()
    review_date = fields.DateTime()
    
class MenuReviewsSchema(Schema):
    menuReview_id = fields.Integer()
    menu_id = fields.Integer()
    rating = fields.Integer()
    review_comment = fields.String()
    review_date = fields.DateTime()
    
class MenuSchema(Schema):
    menu_id = fields.Integer()
    restaurant_id = fields.Integer()
    menu_name = fields.String()
    description = fields.String()
    prices = fields.Integer()
    image = fields.String()
    
class RestaurantSchema(Schema):
    restaurant_id = fields.Integer()
    owner_id = fields.Integer()
    restaurant_name = fields.String()
    contact_number = fields.String()
    opening_hours = fields.Time()
    closing_hours = fields.Time()
    image = fields.String()
    payment_method = fields.String()
    # menus = fields.Nested(MenuSchema, many=True)

class UserSchema(Schema):
    user_id = fields.Integer()
    user_name = fields.String()
    email = fields.String()
    password = fields.String()
    confirm_password = fields.String()
    type = fields.Boolean()
    blocked = fields.String()
    activity = fields.String()
    
class FavouritesSchema(Schema):
  favourite_id = fields.Integer
  user_id = fields.Integer
  menu_id = fields.Integer

class AdminSchema(Schema):
    admin_id = fields.Integer()
    customer_id = fields.Integer()
    restaurant_id = fields.Integer()
    owner_id = fields.Integer()
    name = fields.String()
    password = fields.String()
    
class SuperAdminSchema(Schema):
    superadmin_id = fields.Integer()
    customer_id = fields.Integer()
    restaurant_id = fields.Integer()
    owner_id = fields.Integer()
    name = fields.String()
    password = fields.String()



class CreateSignupInputSchema(Schema):
    # the 'required' argument ensures the field exists
    username = fields.Str(required=True, validate=validate.Length(min=12))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=15))


class CreateLoginInputSchema(Schema):
    # the'required' argument ensures the field exists
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=15))