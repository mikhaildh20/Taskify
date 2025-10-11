from app import db

class Tasks(db.Model):
    __tablename__ = 'tsk_tasks'
    __table_args__ = {'schema':'dbo'}

    id = db.Column('tks_id', db.Integer, primary_key = True)
    fId = db.Column('usr_id', db.Integer, db.ForeignKey('dbo.tsk_users.usr_id'), nullable = False)
    title = db.Column('tks_title', db.String(100), nullable = False)
    description = db.Column('tks_description', db.String(255), nullable = True)
    deadline = db.Column('tks_deadline', db.Date, nullable = False)
    is_done = db.Column('tks_is_done',db.Integer, nullable = True)
    created_at = db.Column('tks_created_at', db.DateTime)
    
    # relation to user model
    user = db.relationship('Users', back_populates = 'tasks')
    
    # relation to time logs model
    timeLogs = db.relationship('TimeLogs', back_populates='task', cascade='all, delete-orphan')

    def to_dict(self, include_user = False, include_timeLogs = False):
        data = {
            "id": self.id,
            "fId": self.fId,
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "is_done": self.is_done,
            "created_at": self.created_at
        }
        if include_user:
            data["user"] = {
                "id": self.user.id,
                "username": self.user.username,
                "email": self.user.email
            }
        if include_timeLogs:
            data["timeLogs"] = [timeLog.to_dict() for timeLog in self.timeLogs]
        return data