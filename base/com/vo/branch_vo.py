from base import db

class BranchVO(db.Model):
    __tablename__='branch_table'
    branch_id=db.Column('branch_id',db.Integer,primary_key=True,autoincrement=True)
    branch_name=db.Column('branch_name',db.String(255),nullable=False)
    branch_country=db.Column('branch_country',db.Integer,db.ForeignKey('country_table.country_id',ondelete='CASCADE',onupdate='CASCADE'),nullable=False)
    branch_state=db.Column('branch_state',db.Integer,db.ForeignKey('state_table.state_id',ondelete='CASCADE',onupdate='CASCADE'),nullable=False)
    branch_city=db.Column('branch_city',db.Integer,db.ForeignKey('city_table.city_id',ondelete='CASCADE',onupdate='CASCADE'),nullable=False)
    branch_contact=db.Column('branch_contact',db.String(255),nullable=False)
    branch_manager=db.Column('branch_manager',db.String(255),nullable=False)
    branch_timings=db.Column('branch_timings',db.String(255),nullable=False)
    branch_days=db.Column('branch_days',db.String(255),nullable=False)

    def as_dict(self):
        return{
            'branch_id':self.branch_id,
            'branch_name':self.branch_name,
            'branch_country':self.branch_country,
            'branch_state':self.branch_state,
            'branch_city':self.branch_city,
            'branch_contact':self.branch_contact,
            'branch_manager':self.branch_manager,
            'branch_timings':self.branch_timings,
            'branch_days':self.branch_days
        }
db.create_all()