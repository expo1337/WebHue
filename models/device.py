from db import db
from datetime import datetime


class DeviceModel(db.Model):
    __tablename__ = 'devices'
    uid = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    bluetooth_address = db.Column(db.String(17))
    user_id = db.Column(db.String(), db.ForeignKey('users.uid'))
    description = db.Column(db.String(1000))
    #user = db.relationship('UserModel', back_populates='devices', cascade='save-update, merge')
    created_at = db.Column(db.TIMESTAMP(timezone=True))
    state_brightness = db.Column(db.String(3))
    state_color = db.Column(db.String(6))
    state_power = db.Column(db.Boolean)

    def __init__(self,name,bluetooth_address, user_id, description):
        self.name = name
        self.bluetooth_address = bluetooth_address
        self.user_id = user_id
        self.created_at = datetime.utcnow()
        self.description = description
        self.state_brightness = '100'
        self.state_color = 'FFFFFF'
        self.state_power = True

    def __str__(self):
        return f"DeviceModel(name='{self.name}', bluetooth_address='{self.bluetooth_address}', uid='{self.uid}', user_id='{self.user_id}', description='{self.description}', state_brightness='{self.state_brightness}', state_color='{self.state_color}', state_power='{self.state_power}')"

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def update_state(self, new_brightness=None, new_color=None, new_power=None):
        db.session.add(self)
        if new_brightness is not None:
            self.state_brightness = new_brightness
        if new_color is not None:
            self.state_color = new_color
        if new_power is not None:
            self.state_power = new_power
        db.session.commit()

    @classmethod
    def find_by_uid(cls, _id):
        return cls.query.filter_by(uid = _id).first()
    
    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id = user_id)
