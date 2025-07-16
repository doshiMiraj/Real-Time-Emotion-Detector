from base import db
from sqlalchemy import select, engine
from base.com.vo.detection_vo import DetectionVO

class DetectionDAO():
    def insert_detection(self,detection_vo):
        db.session.add(detection_vo)
        db.session.commit()

    def view_detection(self):
        detection_vo_list=DetectionVO.query.all()
        return detection_vo_list

    def delete_detection(self,detection_vo):
        detection_vo_list=DetectionVO.query.get(detection_vo.detection_id)
        db.session.delete(detection_vo_list)
        db.session.commit()