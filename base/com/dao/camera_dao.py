from base import db
from base.com.vo.camera_vo import CameraVO

class CameraDAO():
    def insert_camera(self,camera_vo):
        db.session.add(camera_vo)
        db.session.commit()

    def view_camera(self):
        camera_vo_list=CameraVO.query.all()
        return camera_vo_list

    def delete_camera(self,camera_vo):
        camera_vo_list=CameraVO.query.get(camera_vo.camera_id)
        db.session.delete(camera_vo_list)
        db.session.commit()

    def edit_camera(self,camera_vo):
        camera_vo_list=CameraVO.query.filter_by(camera_id=camera_vo.camera_id).all()
        return camera_vo_list

    def update_camera(self,camera_vo):
        db.session.merge(camera_vo)
        db.session.commit()

    def get_camera(self,camera_vo):
        camera_name = CameraVO.query.filter_by(camera_branch_id=camera_vo.camera_branch_id).all()
        return camera_name