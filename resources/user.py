from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)
from passlib.hash import sha256_crypt

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type=str,
    required=True,
    help="This field is required"
    )
    parser.add_argument('password',
    type=str,
    required=True,
    help="This field is required"
    )

    def post (self):
        data = UserRegister.parser.parse_args()
        password_hash_1 = sha256_crypt.encrypt(data['password'])
        user = UserModel(data['username'], password_hash_1)
        user.save_to_db()
        find_user = UserModel.find_by_username(data['username'])
        access_token = create_access_token(identity=data['username'])
        refresh_token = create_refresh_token(identity=data['username'])
        return {"access_token": access_token,
                "refresh_token": refresh_token,
                "user_id": find_user.uid,
                "username": find_user.username,
               "message": "User created successfully."}, 201

class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type=str,
    required=True,
    help="This field is required"
    )
    parser.add_argument('password',
    type=str,
    required=True,
    help="This field is required"
    )

    def post (self):
        data = UserLogin.parser.parse_args()
        find_user = UserModel.find_by_username(data['username'])
        if find_user:
            if sha256_crypt.verify(data['password'], find_user.password):
                access_token = create_access_token(identity=data['username'])
                refresh_token = create_refresh_token(identity=data['username'])
                print(find_user)
                return {"access_token": access_token,
                "refresh_token": refresh_token,
                "user_id": find_user.uid,
                "username": find_user.username,
               "message": "Logged in!."}, 200
            else:
                return {"message": "Login Failed!"}, 401
        else: 
            return {"message": "Login Failed!"}, 401

class DeleteUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type=str,
    required=True,
    help="This field is required")
    parser.add_argument('password',
    type=str,
    required=True,
    help="This field is required")
    def post (self):
        data = UserLogin.parser.parse_args()
        find_user = UserModel.find_by_username(data['username'])
        if find_user:   
            if sha256_crypt.verify(data['password'], find_user.password):
                find_user.delete_from_db()
                return {"message": "User Deleted!"}, 200
            else:
                return {"message": "Incorrect Password!"}, 401
        else: return {"message": "User not found!"}, 404


class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def post (self):
        current_user = get_jwt_identity()
        userdata = UserModel.find_by_username(current_user)
        new_token = create_access_token(identity=current_user)
        return {"access_token": new_token,
        "username": userdata.username,
        "user_id": userdata.uid,
        "message": "Token created!"}, 200     
        