from flask import make_response, abort
from config import db
from models import Restaurant
from models import RestaurantSchema


def get_all_restaurants():

    restaurants = Restaurant.query.order_by(Restaurant.name).all()
    restaurant_schema = RestaurantSchema(many=True)
    return restaurant_schema.dump(restaurants).data


def create_restaurant(body):
    if body is None:
        abort(
            400, "Dude wtf?"
        )

    if body.get("name") is None:
        abort(
            400, "... a man needs a name (and a web)"
        )

    name = body.get("name")
    tmp_res = Restaurant.query.filter(Restaurant.name == name).one_or_none()

    if tmp_res is not None:
        return abort(409, "can't touch this NaNaNaNa")

    else:
        restaurant_schema = RestaurantSchema()
        new_restaurant = restaurant_schema.load(body, session=db.session).data
        db.session.add(new_restaurant)
        db.session.commit()
        return restaurant_schema.dump(new_restaurant).data, 201


def get_restaurant(name):

    if name is None:
        abort(
            400, "Nope"
        )

    restaurant = Restaurant.query.filter(Restaurant.name == name).one_or_none() if not None else abort(400, "not found")

    restaurant_schema = RestaurantSchema()

    return restaurant_schema.dump(restaurant).data


def update_restaurant(name, body):

    restaurant = Restaurant.query.filter(Restaurant.name == name).one_or_none() if not None else abort(400, "not found")
    restaurant_schema = RestaurantSchema()
    update_payload = restaurant_schema.load(body, session=db.session).data
    db.session.merge(update_payload)
    db.session.commit()
    data = restaurant_schema.dump(restaurant).data

    return data, 200


def delete_restaurant(name):

    restaurant = Restaurant.query.filter(Restaurant.name == name).one_or_none()

    if restaurant is None:
        abort(
            400, f"{name} doesn't exist, go delete yourself."
            )
    else:
        db.session.delete(restaurant)
        db.session.commit()
        return make_response(
            f"{name} deleted", 200
        )
