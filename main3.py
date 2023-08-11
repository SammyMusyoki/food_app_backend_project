#app.py
from flask import Flask, request, jsonify, make_response,redirect, url_for
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity,JWTManager,jwt_required
import jwt
from functools import wraps
import uuid
from flask_sqlalchemy import SQLAlchemy
from model import db,User
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = b'\x06\xf5\xb5\xe6\xf7\x1c\xbd\r\xc5e\xef\xb2\xf1\xcb`\xd8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://steve:gzvhtFOUedOgHo9WaG2R5QCfcsXABXI8@dpg-cj5lg1acn0vc73d98li0-a.oregon-postgres.render.com/dbfoodapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

jwt=JWTManager(app)

migrate = Migrate(app, db)
ma = Marshmallow(app)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'username', 'email', 'password', 'user_role', 'blocked', 'activity')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return({"message" : "Token is missing"})

        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
            
        except:
            return ({"message": "Invalid token"})

        return f(*args, **kwargs)
    return decorated

@app.route('/superadmin/<token>')
@jwt_required(optional=True)
def superadmin(token):
    return jsonify(token=f"superadmin : {token}")

@app.route('/admin/<token>')
@jwt_required(optional=True)
def admin(token):
    return jsonify(token=f"admin : {token}")

@app.route('/customer/<token>')
@jwt_required(optional=True)
def customer(token):
    return jsonify(token=f"student : {token}")

@app.route('/driver/<token>')
@jwt_required(optional=True)
def driver(token):
    return jsonify(token=f"driver : {token}")

@app.route('/orders')
@jwt_required(optional=True)
def orders():
    details = get_jwt()
    if details["user_role"]!='driver':
        return redirect(url_for("guest"))
    return jsonify(detail="info")

@app.route('/guest')
@jwt_required()
def guest():
    details = get_jwt()
    return jsonify(detail=f"welcome {details['username']}")
    
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.json.get('email',None)
        password = request.json.get('password',None)
        user = User.query.filter_by(email=email).first()
        if user:
            if user.confirm_password(password):
                metadata = {
                   "user_role":user.user_role,
                   "username":user.username
                }
                token = create_access_token(identity=user.user_id, additional_claims=metadata)
                return redirect(url_for(f'{user.user_role}',token=token))
                # return jsonify(token=token)
            return jsonify(detail="password Incorrect"),401
        return jsonify(detail="User not logged in"),401

@app.route('/user', methods=['GET'])
def get_all_users():
     users = User.query.all()

     output = []

     for user in users:
        user_data = {}
        user_data['user_id'] = user.user_id
        user_data['username'] = user.username
        user_data['email'] = user.email
        user_data['password'] = user.password
        user_data['user_role'] = user.user_role
        user_data['blocked'] = user.blocked
        user_data['activity'] = user.activity
        output.append(user_data)
     return jsonify({'users': output})

 
@app.route('/user/<user_id>', methods=['GET'])
def get_one_users(user_id):

    user = User.query.filter_by(user_id=user_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})
    
    user_data = {}
    user_data['user_id'] = user.user_id
    user_data['username'] = user.username
    user_data['email'] = user.email
    user_data['password'] = user.password
    user_data['user_role'] = user.user_role
    user_data['blocked'] = user.blocked
    user_data['activity'] = user.activity
    return jsonify({'users': user_data})
    # pass
 
@app.route('/user', methods=['POST'])
def user():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='scrypt')

    new_user = User(username=data['username'],password=hashed_password, email=data['email'],user_role=data['user_role'],blocked=False,activity=False)
    db.session.add(new_user)
    db.session.commit()
    
    return ({'message':'Welcome user'})

@app.route('/user/<user_id>', methods=['PATCH'])
def promote_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})
    
    user.admin = True
    db.session.commit()

    return jsonify({'message': 'User promoted successfully'})

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'User has been deleted'})

@app.route('/cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):

    product = Product.query.filter(Product.id == product_id)
    cart_item = CartItem(product=product)
    db.session.add(cart_item)
    db.session.commit()

    return jsonify({'message': 'User has been deleted'})

    # return render_tempate('home.html', product=products)
if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
