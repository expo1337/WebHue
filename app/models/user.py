from db import db
from datetime import datetime
from models.device import DeviceModel

class UserModel(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))
    created_at = db.Column(db.TIMESTAMP(timezone=True))

    #user_devices = db.relationship('DeviceModel', back_populates='users', lazy='dynamic', cascade='delete, save-update, merge')

    def __init__(self,username,password):
        self.username = username
        self.password = password 
        self.created_at = datetime.utcnow()

    def __str__(self):
        return f"UserModel(username='{self.username}', password='{self.password}', uid='{self.uid}')"

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_uid(cls, _id):
        return cls.query.filter_by(uid = _id).first()
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()