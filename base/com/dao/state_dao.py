from base import db
from sqlalchemy import select, engine
from base.com.vo.state_vo import StateVO


class StateDAO():
    def insert_state(self, state_vo):
        db.session.add(state_vo)
        db.session.commit()

    def view_state(self):
        state_vo_list = StateVO.query.all()
        return state_vo_list

    def get_state(self, state_vo):
        state_vo_list = StateVO.query.filter_by(state_country_id=state_vo.state_country_id).all()
        return state_vo_list


