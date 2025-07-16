from base import db
from sqlalchemy import select, engine
from base.com.vo.country_vo import CountryVO

class CountryDAO():
    def insert_country(self,country_vo):
        db.session.add(country_vo)
        db.session.commit()
    def view_country(self):
        country_vo_list=CountryVO.query.all()
        return country_vo_list
