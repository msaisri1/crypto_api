from flask import Flask, request, jsonify
from flask import Flask, request, jsonify
import requests
from models import *
from schemas import *
from flask_httpauth import HTTPBasicAuth
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token,get_jwt_identity

from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_bcrypt import Bcrypt
import json

from flask_swagger_ui import get_swaggerui_blueprint




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt = Bcrypt(app)


# Set up JWT
app.config["JWT_SECRET_KEY"] = "my-secret-key"
jwt = JWTManager(app)


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Api Project'
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)






@app.route('/api/v3/markets/summaries', methods=['GET'])
@jwt_required()
def market_data():
    response = requests.get('https://api.bittrex.com/v3/markets/summaries', verify = False)
    markets = response.json()
    return jsonify({'result':markets,'message': 'markets data received'})





@app.route('/api/v3/markets/<string:id>/summary', methods=['GET'])
@jwt_required()
def get_market_by_id(id):
    response = requests.get('https://api.bittrex.com/v3/markets/'+id+'/summary', verify = False)
    market = response.json()
   

    return jsonify(market)








# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # Hash the password
    hashed_password = generate_password_hash(data['password'])
    # Save the user to the database
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': "successfully registered"}), 201
    
   


# Route to login a user
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # Get the user from the database
    user = User.query.filter_by(username=data['username']).first()
    # Check if the user exists and the password is correct
    if user and check_password_hash(user.password, data['password']):
        # Create an access token for the user
        access_token = create_access_token(identity=data['username'])
        return jsonify({'message': 'Logged in', 'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


# Protected route
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({'message': 'Access granted', 'current_user': current_user}), 200






if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)