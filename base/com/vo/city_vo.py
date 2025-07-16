from base import db


class CityVO(db.Model):
    __tablename__ = 'city_table'
    city_id = db.Column('city_id', db.Integer, primary_key=True, autoincrement=True)
    city_name = db.Column('city_name', db.String(255), nullable=False)
    city_country_id = db.Column('city_country_id', db.Integer,
                                db.ForeignKey('country_table.country_id', ondelete="CASCADE", onupdate="CASCADE"),
                                nullable=False)
    city_state_id = db.Column('city_state_id', db.Integer,
                              db.ForeignKey('state_table.state_id', ondelete="CASCADE", onupdate="CASCADE"),
                              nullable=False)

    def as_dict(self):
        return {'city_id': self.city_id, 'city_name': self.city_name, 'city_country_id': self.city_country_id,
            'city_state_id': self.city_state_id}


db.create_all()