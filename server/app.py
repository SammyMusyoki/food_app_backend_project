from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from datetime import datetime
from flask_marshmallow import Marshmallow
from models import db
from schemas import *
from main2 import main2
from mpesa import mpesa
from Stripe import stripe
from werkzeug.wrappers import Response 
from flask_restful import Api


from Restaurant import restaurants
from User import user
from Owner import owners
from Reviews import reviews
# from Stripe import stripe




app = Flask(__name__) 
app.register_blueprint(main2)
app.register_blueprint(restaurants)
app.register_blueprint(user)
app.register_blueprint(owners)
app.register_blueprint(reviews)
app.register_blueprint(mpesa)
app.register_blueprint(stripe)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://steve:gzvhtFOUedOgHo9WaG2R5QCfcsXABXI8@dpg-cj5lg1acn0vc73d98li0-a.oregon-postgres.render.com/dbfoodapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)
CORS(app)


ma = Marshmallow(app)

api = restful.Api(app=app)

from Auth.routes import create_authentication_routes

create_authentication_routes(api=api)

@app.before_request
def before_request():
    if request.method == ['OPTIONS', 'POST', 'PUT', 'DELETE', 'HEAD']:
        response = Response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"
        response.headers["Access-Control-Allow-Methods"] = '*'
        return response

# def _build_cors_preflight_response():
#     response = make_response()
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     response.headers.add('Access-Control-Allow-Headers', "*")
#     response.headers.add('Access-Control-Allow-Methods', "*")
#     return response


# @app.route('/')
# def index():
#     return {"message": "success"}
db.init_app(app)
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
