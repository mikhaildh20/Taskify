from app import db

class Tasks(db.Model):
    __tablename__ = 'tsk_tasks'
    __table_args__ = {'schema':'dbo'}

    id = db.Column('tks_id', db.Integer, primary_key = True)
    fId = db.Column('usr_id', db.Integer, nullable = False)
    title = db.Column('tks_title', db.String(100), nullable = False)
    description = db.Column('tks_description', db.String(255), nullable = True)
    deadline = db.Column('tks_deadline', db.Date, nullable = False)
    is_done = db.Column('tks_is_done',db.Integer, nullable = True)
    created_at = db.Column('tks_created_at', db.DateTime)

    def to_dict(self):
        return {
            "id": self.id,
            "fId": self.fId,
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "is_done": self.is_done,
            "created_at": self.is_done
        }