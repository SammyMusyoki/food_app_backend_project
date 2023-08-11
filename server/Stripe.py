from flask import Flask, jsonify, request,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from datetime import datetime
from flask_marshmallow import Marshmallow
import stripe
stripe = Blueprint("Stripe",__name__)
ma = Marshmallow()


app = Flask(__name__)
ma.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://steve:gzvhtFOUedOgHo9WaG2R5QCfcsXABXI8@dpg-cj5lg1acn0vc73d98li0-a.oregon-postgres.render.com/dbfoodapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app, origins="http://localhost:5000") 

stripe.api_key = "sk_test_51NaCrLDWZ8VYT067qJD7GMGRRTzNesXgPuOtirmWozS1Ntg6srUUfwu6Mo03Mrm1W5AZOZqTacuzk9LeKrNgvJ9y00re0LPdjZ"



@stripe.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    try:
        data = request.get_json()
        amount = data['amount']  

        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
        )

        return jsonify(client_secret=intent.client_secret)
    except Exception as e:
        return jsonify(error=str(e)), 500

