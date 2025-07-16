from base import db


class DetectionVO(db.Model):
    __tablename__ = 'detection_table'
    detection_id = db.Column('detection_id', db.Integer, primary_key=True, autoincrement=True)
    detection_branch_id = db.Column('detection_branch_id', db.Integer,
                                    db.ForeignKey('branch_table.branch_id', ondelete='CASCADE', onupdate='CASCADE'),
                                    nullable=False)
    detection_camera_id = db.Column('detection_camera_id', db.Integer,
                                    db.ForeignKey('camera_table.camera_id', ondelete='CASCADE', onupdate='CASCADE'),
                                    nullable=False)
    angry_count=db.Column('angry_count',db.String(255),nullable=True)
    disgust_count = db.Column('disgust_count', db.String(255), nullable=True)
    fear_count = db.Column('fear_count', db.String(255), nullable=True)
    happy_count = db.Column('happy_count', db.String(255), nullable=True)
    sad_count = db.Column('sad_count', db.String(255), nullable=True)
    surprise_count = db.Column('surprise_count', db.String(255), nullable=True)
    neutral_count = db.Column('neutral_count', db.String(255), nullable=True)
    detection_date=db.Column('detection_date',db.String(255),nullable=True)
    detection_time = db.Column('detection_time', db.String(255), nullable=True)

    def as_dict(self):
        return {
            'detection_id':self.detection_id,
            'detection_branch_id':self.detection_branch_id,
            'detection_camera_id':self.detection_camera_id,
            'angry_count':self.angry_count,
            'disgust_count':self.disgust_count,
            'fear_count':self.fear_count,
            'happy_count':self.happy_count,
            'sad_count':self.sad_count,
            'surprise_count':self.surprise_count,
            'neutral_count':self.neutral_count,
            'detection_date':self.detection_date,
            'detection_time':self.detection_time
        }

db.create_all()