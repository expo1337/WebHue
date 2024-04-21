from flask_restful import Resource, reqparse
from flask import jsonify
from models.user import UserModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)
from models.device import DeviceModel
import json
import asyncio
from resources.bluetooth import Bluetooth

class DeviceAdd(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
    type=str,
    required=True,
    help="This field is required"
    )
    parser.add_argument('bluetooth_address',
    type=str,
    required=True,
    help="This field is required"
    )
    parser.add_argument('user_id',
    type=str,
    required=True,
    help="This field is required"
    )
    parser.add_argument('description',
    type=str,
    required=False,
    help="Device Description")

    def post (self):
        data = DeviceAdd.parser.parse_args()
        device = DeviceModel(data['name'], data['bluetooth_address'], data['user_id'], data['description'])
        device.save_to_db()
        return {"message": "Device created successfully."}, 201

class GetUserDevices(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        userdata = UserModel.find_by_username(current_user)
        devices = DeviceModel.find_by_user_id(userdata.uid)
        device_list = []
        if devices:
            for device in devices:
                device_dict = {
                    'uid': device.uid,
                    'name': device.name,
                    'bluetooth_address': device.bluetooth_address,
                    'description': device.description,
                    'brightness': device.state_brightness,
                    'color': device.state_color,
                    'power': device.state_power
                }
                device_list.append(device_dict)
                print(device_dict)
            if not device_list: 
                print(device_list)
            response_list = json.dumps(device_list)
            return {"devices": response_list, "message": "Device fetch successfull!"}, 200
        else: 
            return {"message": "No devices found!"}, 404

class SendDeviceCommand(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('address',
    type=str,
    required=True,
    help="This field is required"
    )
    parser.add_argument('command',
    type=str,
    required=True,
    help="This field is required"
    )
    @jwt_required()
    def post(self):
        data = SendDeviceCommand.parser.parse_args()
        asyncio.run(Bluetooth.sendCommand(data['command'], data['address']))
        return {"Message": "Command executed successfully!"}, 200


class SendDeviceCommandCustomUuid(Resource): 
    parser = reqparse.RequestParser()
    parser.add_argument('address',
    type=str,
    required=True,
    help="This field is required"
    )
    parser.add_argument('command',
    type=str,
    required=True,
    help="This field is required"
    )
    parser.add_argument('uuid',
    type=str,
    required=True,
    help="This field is required"
    )
    @jwt_required()
    def post(self):
        data = SendDeviceCommandCustomUuid.parser.parse_args()
        try:
            asyncio.run(Bluetooth.sendCommandCustomUuid(data['command'], data['address'], data['uuid']))
            return {
                "Message": "Command executed successfully!"
            }, 200
        except Exception as e:
            return {
                "Message": "Device not found, check power and bluetooth range",
                "Exception": str(e),
            }, 404

class CheckDeviceStatus(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('address',
    type=str,
    required=True,
    help="This field is required"
    )
    @jwt_required()
    def get(self):
        data = CheckDeviceStatus.parser.parse_args()
        in_range = asyncio.run(Bluetooth.checkDeviceStatus(data['address']))
        if in_range:
            return {
                "Device": "True"
            }, 200
        else:
            return {
                "Device": "False",
            }, 200

class DeleteDevice(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uid',
    type=str,
    required=True,
    help="This field is required")
    @jwt_required()
    def post(self):
        data = DeleteDevice.parser.parse_args()
        current_user = get_jwt_identity()
        userdata = UserModel.find_by_username(current_user)
        device = DeviceModel.find_by_uid(data['uid'])
        if device: 
            if str(userdata.uid) == str(device.user_id): 
                device.delete_from_db()
                return {"message": "Device Deleted!"}, 200
            else:
                return {"message": "Device not found!"}, 404
        else: 
            return {"message": "Device not found!"}, 404

class UpdateDeviceState(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uid',
    type=str,
    required=True,
    help="This field is required")
    parser.add_argument('brightness',
    type=str,
    required=False)
    parser.add_argument('color',
    type=str,
    required=False)
    parser.add_argument('power',
    type=str,
    required=False)
    @jwt_required()
    def post(self):
        data = UpdateDeviceState.parser.parse_args()
        device = DeviceModel.find_by_uid(data['uid'])
        brightness = data.get('brightness')
        color = data.get('color')
        power = data.get('power')
        if device:
            if brightness is not None:
                device.update_state(new_brightness = data['brightness'])
            if color is not None:
                device.update_state(new_color = data['color'])
            if power is not None:
                if power == 'True':
                    device.update_state(new_power=True)
                else:
                    device.update_state(new_power=False)    
            return {"message": "Device state updated!"}, 200
        else:
            return {"message": "Device not found!"}, 404

class GetNearbyDevices(Resource):
    @jwt_required()
    def get(self):
        nearby_devices = asyncio.run(Bluetooth.findNearbyDevices())
        print(nearby_devices)
        if nearby_devices:
            #return {"nearby_devices": json.dumps({"devices": nearby_devices})}, 200
            return {"nearby_devices": json.dumps(nearby_devices)}, 200
        else:
            return {"message": "No devices found!"}, 404

class GetDeviceServices(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('address',
    type=str,
    required=True,
    help="This field is required")
    @jwt_required()
    def post(self):
        data = GetDeviceServices.parser.parse_args()
        device = data.get('address')
        services = asyncio.run(Bluetooth.findDeviceServices(device))
        if services:
            return {"services": json.dumps(services)}, 200
        else:
            return {"message": "No services found!"}, 404
        
