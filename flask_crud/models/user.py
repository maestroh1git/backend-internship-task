from sqlalchemy import Column, String, ForeignKey
import uuid
from flask_crud import db

def generate_uuid():
    return str(uuid.uuid4())

class User(db.Model):
    id = Column(String(36), primary_key=True, default=generate_uuid)
    username = Column(String(80), unique=True, nullable=False)
    password_hash = Column(String(120), nullable=False)
    role_id = Column(String(36), ForeignKey('role.id'), nullable=False)

    role = db.relationship('Role', backref='users')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'role_id': self.role_id,
        }