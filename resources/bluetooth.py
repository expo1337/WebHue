import asyncio 
from bleak import BleakClient, BleakScanner
import numpy
import math

class Bluetooth:
    async def sendCommand (command, address):
        uuid = "0000fff3-0000-1000-8000-00805f9b34fb"
        async with BleakClient(address) as client:
            send_command = await client.write_gatt_char(uuid, bytes.fromhex(command))
    
    async def sendCommandCustomUuid (command, address, custom_uuid):
        async with BleakClient(address) as client:
            send_command = await client.write_gatt_char(custom_uuid, bytes.fromhex(command))

    async def checkDeviceStatus (address):
        devices = await BleakScanner.discover()
        for device in devices:
            if device.address.upper() == address.upper():
                return True
            else:
                return False
    
    async def findNearbyDevices():
        devices = await BleakScanner.discover(True)
        device_id = 0 
        device_count = 0
        nearby_devices = []
        if devices:
            for device in devices:
                device_id += 1
                device_info = {
                    "id": device_id,
                    "name": device.name,
                    "address": device.address,
                }
                device_count += 1
                nearby_devices.append(device_info)
            new_array = numpy.array_split(nearby_devices, math.floor(device_count/10+1))
            new_array_as_list = [sub_array.tolist() for sub_array in new_array]
            return new_array_as_list
        else:
            return []
    
    async def findDeviceServices(address):
        services = {"uuid": "xd", "chars": []}  # Initialize services as a dictionary
        device = await BleakScanner.find_device_by_address(address)
        if device is None:
            return []
        async with BleakClient(device) as client: 
            for service in client.services:
                #service['uuid'] = str(service.uuid)
                for char in service.characteristics:
                    try:
                        value = await client.read_gatt_char(char.uuid)
                        new_string = "  [Characteristic] {} ({}), Value: {}".format(
                            char.uuid,  # Assuming char is an object with a uuid attribute
                            ",".join(char.properties),
                            value
                        )
                        services['chars'].append(new_string)
                    except Exception as e:
                        new_string = "  [Characteristic] {} ({}) Error: {}".format(
                            char.uuid,  # Assuming char is an object with a uuid attribute
                            ",".join(char.properties),
                            e,
                        )
                        services['chars'].append(new_string)
        return services

