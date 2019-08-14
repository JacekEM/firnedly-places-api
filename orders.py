
orders = {}


def create_order(body):

    name = body.get("name", None)
    orders[name] = body
