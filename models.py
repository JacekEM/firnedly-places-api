from config import db, ma


class Restaurant(db.Model):

    __tablename__ = 'restaurants'

    res_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    address = db.Column(db.String(50), nullable=True)
    web = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.Integer)


class RestaurantSchema(ma.ModelSchema):

    class Meta:

        model = Restaurant

        sql_session = db.session
