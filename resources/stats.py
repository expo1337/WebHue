from db import db
from datetime import datetime
from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)
import psutil

def GetCpuUsage():
    cpu_usage = psutil.cpu_percent(0)
    return str(cpu_usage)

def GetRamUsage():
    ram_usage = psutil.virtual_memory()[2]
    return str(ram_usage)

class GetStats(Resource):
    @jwt_required()
    def get(self):
        cpu_usage = GetCpuUsage()
        ram_usage = GetRamUsage()
        return {"ram_usage": ram_usage,
                "cpu_usage": cpu_usage,
                "message": "Got Stats!"}, 200   
    

