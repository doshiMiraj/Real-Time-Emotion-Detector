from base import db

class StateVO(db.Model):
    __tablename__="state_table"
    state_id=db.Column('state_id',db.Integer,primary_key=True,autoincrement=True)
    state_name = db.Column('state_name', db.String(255),nullable=False)
    state_country_id = db.Column('state_country_id', db.Integer,db.ForeignKey('country_table.country_id',ondelete="CASCADE",onupdate="CASCADE"),nullable=False)

    def as_dict(self):
        return{
            'state_id':self.state_id,
            'state_name':self.state_name,
            'state_country_id':self.state_country_id
        }

db.create_all()
