from app import db

class TimeLogs(db.Model):
    __tablename__ = 'tsk_time_logs'
    __table_args__ = {'schema': 'dbo'}
    
    id = db.Column('tlg_id', db.Integer, primary_key = True)
    fId = db.Column('tks_id', db.Integer, db.ForeignKey('dbo.tsk_tasks.tks_id'), nullable = False)
    startTime = db.Column('tlg_start_time', db.DateTime, nullable = False)
    endTime = db.Column('tlg_end_time', db.DateTime, nullable = False)
    duration = db.Column('tlg_duration', db.Integer, nullable = True)
    
    # relation to task model
    task = db.relationship('Tasks', back_populates='timeLogs')
    
    def to_dict(self, include_task = False):
        data = {
            "id": self.id,
            "fId": self.fId,
            "startTime": self.startTime,
            "endTime": self.endTime,
            "duration": self.duration
        }
        if include_task:
            data['task'] = {
                "id": self.task.id,
                "title": self.task.title,
                "description": self.task.description,
                "deadline": self.task.deadline,
                "is_done": self.task.is_done,
            }
        return data