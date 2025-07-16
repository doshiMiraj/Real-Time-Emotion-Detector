from base.com.vo.city_vo import CityVO
from base import db
from sqlalchemy import select, engine

class CityDAO():
    def insert_city(self,city_vo):
        db.session.add(city_vo)
        db.session.commit()
    def view_city(self):
        city_vo_list=CityVO.query.all()
        return city_vo_list

    def get_city(self,city_vo):
        city_name=CityVO.query.filter_by(city_state_id=city_vo.city_state_id).all()
        return city_name