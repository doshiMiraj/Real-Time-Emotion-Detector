from base import db

class CameraVO(db.Model):
    __tablename__='camera_table'
    camera_id=db.Column('camera_id',db.Integer,primary_key=True,autoincrement=True)
    camera_name=db.Column('camera_name',db.String(255),nullable=False)
    camera_model=db.Column('camera_model',db.String(255),nullable=False)
    camera_location=db.Column('camera_location',db.String(255),nullable=False)
    camera_branch_id=db.Column('camera_branch_id',db.Integer,db.ForeignKey('branch_table.branch_id',ondelete='CASCADE',onupdate="CASCADE"),nullable=False)
    camera_field_of_vision=db.Column('camera_field_of_vision',db.String(255),nullable=False)
    camera_resolution=db.Column('camera_resolution',db.String(255),nullable=False)
    camera_recording_mode=db.Column("camera_recording_mode",db.String(255),nullable=False)

    def as_dict(self):
        return{
            'camera_id':self.camera_id,
            'camera_name':self.camera_name,
            'camera_model':self.camera_model,
            'camera_location':self.camera_location,
            'camera_branch_id':self.camera_branch_id,
            'camera_field_of_vision':self.camera_field_of_vision,
            'camera_resolution':self.camera_resolution,
            'camera_recording_mode':self.camera_recording_mode
        }

db.create_all()
