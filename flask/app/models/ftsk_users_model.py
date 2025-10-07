from app import db

class Users(db.Model):
    __tablename__ = 'tsk_users'
    __table_args__ = {'schema': 'dbo'}
    
    id = db.Column('usr_id', db.Integer, primary_key = True)
    username = db.Column('usr_username', db.String(50), nullable = False)
    email = db.Column('usr_email', db.String(100), nullable = False)
    password = db.Column('usr_password', db.String(255), nullable = False)
    created_at = db.Column('usr_created_at', db.DateTime)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at
        }

