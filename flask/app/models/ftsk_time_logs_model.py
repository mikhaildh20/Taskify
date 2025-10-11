from app import db

class TimeLogs(db.Model):
    __tablename__ = 'tsk_time_logs'
    __table_args__ = {'schema': 'dbo'}
    
    id = db.Column('tlg_id', db.Integer, primary_key = True)
    fId = db.Column('tks_id', db.Integer, nullable = False)
    startTime = db.Column('tlg_start_time', db.DateTime, nullable = False)
    endTime = db.Column('tlg_end_time', db.DateTime, nullable = False)
    duration = db.Column('tlg_duration', db.Integer, nullable = True)
    
    def to_dict(self):
        return{
            "id": self.id,
            "fId": self.fId,
            "startTime": self.startTime,
            "endTime": self.endTime,
            "duration": self.duration
        }