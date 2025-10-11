from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Users(db.Model):
    __tablename__ = 'tsk_users'
    __table_args__ = {'schema': 'dbo'}
    
    id = db.Column('usr_id', db.Integer, primary_key = True)
    username = db.Column('usr_username', db.String(50), nullable = False)
    email = db.Column('usr_email', db.String(100), nullable = False)
    password_hash = db.Column('usr_password', db.String(255), nullable = False)
    created_at = db.Column('usr_created_at', db.DateTime, default = datetime.utcnow)
    
    # relation to task model
    tasks = db.relationship('Tasks', back_populates='user', cascade='all, delete-orphan')

    def to_dict(self, include_tasks=False):
        data = {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at
        }
        if include_tasks : 
            data["tasks"] = [task.to_dict() for task in self.tasks]
        return data

