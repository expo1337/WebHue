import os
import logging
from flask import Flask 
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from resources.user import UserRegister, UserLogin, TokenRefresh, DeleteUser
from resources.device import DeviceAdd, GetUserDevices, SendDeviceCommand, SendDeviceCommandCustomUuid, CheckDeviceStatus, DeleteDevice, GetNearbyDevices, UpdateDeviceState, GetDeviceServices
from resources.stats import GetStats

app = Flask(__name__)
api = Api(app)
#CORS(app)
CORS(app, origins='*', allow_headers='*', supports_credentials=True)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'd5fb8c4fa8bd46638dadc4e751e0d68d'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 1000
jwt = JWTManager(app)

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/token_refresh')
api.add_resource(DeviceAdd, '/add_device')
api.add_resource(GetUserDevices, '/get_devices')
api.add_resource(GetStats, '/get_stats')
api.add_resource(DeleteUser, '/delete_user')
api.add_resource(SendDeviceCommand, '/send_command')
api.add_resource(SendDeviceCommandCustomUuid, '/send_command_custom_uuid')
api.add_resource(CheckDeviceStatus, '/check_device_status')
api.add_resource(DeleteDevice, '/delete_device')
api.add_resource(GetNearbyDevices, '/get_nearby_devices')
api.add_resource(UpdateDeviceState, '/update_device')
api.add_resource(GetDeviceServices, '/get_device_services')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0')